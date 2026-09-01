import pytest

from src.models import Document, SearchResult
from src.reranker import rank_scored_candidates


def make_candidate(
    document_id: str,
    rank: int,
) -> SearchResult:
    return SearchResult(
        document=Document(
            id=document_id,
            title=f"Document {document_id}",
            text=f"Text for document {document_id}",
        ),
        score=0.0,
        rank=rank,
    )


def test_candidates_are_sorted_by_cross_encoder_score() -> None:
    candidates = [
        make_candidate("A", rank=1),
        make_candidate("B", rank=2),
        make_candidate("C", rank=3),
    ]

    scores = [0.10, 0.90, 0.40]

    results = rank_scored_candidates(
        candidates=candidates,
        scores=scores,
        top_k=3,
    )

    assert [
        result.document.id
        for result in results
    ] == ["B", "C", "A"]

    assert [
        result.rank
        for result in results
    ] == [1, 2, 3]

    assert results[0].score == pytest.approx(0.90)


def test_only_top_k_results_are_returned() -> None:
    candidates = [
        make_candidate("A", rank=1),
        make_candidate("B", rank=2),
        make_candidate("C", rank=3),
    ]

    results = rank_scored_candidates(
        candidates=candidates,
        scores=[0.20, 0.80, 0.40],
        top_k=2,
    )

    assert len(results) == 2
    assert results[0].document.id == "B"
    assert results[1].document.id == "C"


def test_candidate_score_count_must_match() -> None:
    candidates = [
        make_candidate("A", rank=1),
        make_candidate("B", rank=2),
    ]

    with pytest.raises(
        ValueError,
        match="Candidate and score counts",
    ):
        rank_scored_candidates(
            candidates=candidates,
            scores=[0.5],
            top_k=2,
        )
