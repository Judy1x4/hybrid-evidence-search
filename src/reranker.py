from collections.abc import Sequence
from typing import Protocol

import numpy as np
import torch
from sentence_transformers import CrossEncoder

from src.models import SearchResult


DEFAULT_MODEL_NAME = (
    "cross-encoder/ms-marco-MiniLM-L6-v2"
)


class Retriever(Protocol):
    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        ...


def rank_scored_candidates(
    candidates: list[SearchResult],
    scores: Sequence[float] | np.ndarray,
    top_k: int,
) -> list[SearchResult]:
    if top_k <= 0:
        raise ValueError(
            "top_k must be greater than zero."
        )

    if len(candidates) != len(scores):
        raise ValueError(
            "Candidate and score counts do not match."
        )

    scored_candidates = [
        (candidate, float(score))
        for candidate, score in zip(candidates, scores)
    ]

    # Use the original hybrid rank as a deterministic
    # secondary ordering rule when scores are equal.
    scored_candidates.sort(
        key=lambda item: (
            -item[1],
            item[0].rank,
            item[0].document.id,
        )
    )

    return [
        SearchResult(
            document=candidate.document,
            score=score,
            rank=new_rank,
        )
        for new_rank, (candidate, score) in enumerate(
            scored_candidates[:top_k],
            start=1,
        )
    ]


class CrossEncoderReranker:
    def __init__(
        self,
        candidate_retriever: Retriever,
        model_name: str = DEFAULT_MODEL_NAME,
        candidate_k: int = 20,
        batch_size: int = 16,
        max_length: int = 512,
    ) -> None:
        if candidate_k <= 0:
            raise ValueError(
                "candidate_k must be greater than zero."
            )

        if batch_size <= 0:
            raise ValueError(
                "batch_size must be greater than zero."
            )

        if max_length <= 0:
            raise ValueError(
                "max_length must be greater than zero."
            )

        self.candidate_retriever = candidate_retriever
        self.model_name = model_name
        self.candidate_k = candidate_k
        self.batch_size = batch_size

        self.model = CrossEncoder(
            model_name,
            max_length=max_length,
            activation_fn=torch.nn.Sigmoid(),
        )

    def rerank(
        self,
        query: str,
        candidates: list[SearchResult],
        top_k: int = 10,
    ) -> list[SearchResult]:
        if not query.strip():
            return []

        if not candidates:
            return []

        pairs = [
            (
                query,
                candidate.document.searchable_text,
            )
            for candidate in candidates
        ]

        scores = self.model.predict(
            pairs,
            batch_size=self.batch_size,
            show_progress_bar=False,
            convert_to_numpy=True,
        )

        scores = np.asarray(scores).reshape(-1)

        return rank_scored_candidates(
            candidates=candidates,
            scores=scores,
            top_k=top_k,
        )

    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        if not query.strip():
            return []

        if top_k <= 0:
            raise ValueError(
                "top_k must be greater than zero."
            )

        candidate_depth = max(
            self.candidate_k,
            top_k,
        )

        candidates = self.candidate_retriever.search(
            query,
            top_k=candidate_depth,
        )

        return self.rerank(
            query=query,
            candidates=candidates,
            top_k=top_k,
        )

    def warm_up(self) -> None:
        self.model.predict(
            [
                (
                    "scientific evidence",
                    "Example scientific document.",
                )
            ],
            batch_size=1,
            show_progress_bar=False,
            convert_to_numpy=True,
        )
