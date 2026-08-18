from collections import defaultdict
from typing import Protocol

from src.models import SearchResult


class Retriever(Protocol):
    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        ...


class HybridRetriever:
    def __init__(
        self,
        bm25_retriever: Retriever,
        dense_retriever: Retriever,
        candidate_k: int = 30,
        rrf_k: int = 60,
    ) -> None:
        if candidate_k <= 0:
            raise ValueError(
                "candidate_k must be greater than zero."
            )

        if rrf_k < 0:
            raise ValueError(
                "rrf_k cannot be negative."
            )

        self.bm25_retriever = bm25_retriever
        self.dense_retriever = dense_retriever
        self.candidate_k = candidate_k
        self.rrf_k = rrf_k

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

        # Ensure enough candidates are retrieved if callers
        # request more results than the configured depth.
        candidate_k = max(self.candidate_k, top_k)

        bm25_results = self.bm25_retriever.search(
            query,
            top_k=candidate_k,
        )

        dense_results = self.dense_retriever.search(
            query,
            top_k=candidate_k,
        )

        rrf_scores: dict[str, float] = defaultdict(float)
        documents_by_id = {}
        best_component_rank: dict[str, int] = {}

        for ranking in (bm25_results, dense_results):
            for result in ranking:
                document_id = result.document.id

                documents_by_id[document_id] = result.document

                rrf_scores[document_id] += (
                    1.0 / (self.rrf_k + result.rank)
                )

                previous_rank = best_component_rank.get(
                    document_id
                )

                if (
                    previous_rank is None
                    or result.rank < previous_rank
                ):
                    best_component_rank[document_id] = (
                        result.rank
                    )

        ranked_document_ids = sorted(
            documents_by_id,
            key=lambda document_id: (
                -rrf_scores[document_id],
                best_component_rank[document_id],
                document_id,
            ),
        )

        ranked_document_ids = ranked_document_ids[:top_k]

        return [
            SearchResult(
                document=documents_by_id[document_id],
                score=rrf_scores[document_id],
                rank=rank,
            )
            for rank, document_id in enumerate(
                ranked_document_ids,
                start=1,
            )
        ]
