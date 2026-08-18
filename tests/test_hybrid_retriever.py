from src.hybrid_retriever import HybridRetriever
from src.models import Document, SearchResult


class FakeRetriever:
    def __init__(
        self,
        results: list[SearchResult],
    ) -> None:
        self.results = results

    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        return self.results[:top_k]


def make_result(
    document: Document,
    rank: int,
) -> SearchResult:
    return SearchResult(
        document=document,
        score=1.0,
        rank=rank,
    )


def test_rrf_promotes_document_found_by_both_systems() -> None:
    document_a = Document(
        id="A",
        title="Document A",
        text="Text A",
    )

    document_b = Document(
        id="B",
        title="Document B",
        text="Text B",
    )

    document_c = Document(
        id="C",
        title="Document C",
        text="Text C",
    )

    bm25 = FakeRetriever(
        [
            make_result(document_a, rank=1),
            make_result(document_b, rank=2),
        ]
    )

    dense = FakeRetriever(
        [
            make_result(document_c, rank=1),
            make_result(document_a, rank=2),
        ]
    )

    hybrid = HybridRetriever(
        bm25_retriever=bm25,
        dense_retriever=dense,
        candidate_k=10,
        rrf_k=60,
    )

    results = hybrid.search(
        "example query",
        top_k=3,
    )

    assert len(results) == 3
    assert results[0].document.id == "A"

    scores = [result.score for result in results]

    assert scores == sorted(scores, reverse=True)


def test_empty_query_returns_no_results() -> None:
    retriever = FakeRetriever([])

    hybrid = HybridRetriever(
        bm25_retriever=retriever,
        dense_retriever=retriever,
    )

    assert hybrid.search("   ") == []
