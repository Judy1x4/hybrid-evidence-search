import math
import time

from typing import Protocol
from src.models import SearchResult

class Retriever(Protocol):
    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        ...

def recall_at_k(
    ranked_document_ids: list[str],
    relevant_documents: dict[str, int],
    k: int,
) -> float:
    relevant_ids = {
        document_id
        for document_id, relevance in relevant_documents.items()
        if relevance > 0
    }

    if not relevant_ids:
        return 0.0

    retrieved_ids = set(ranked_document_ids[:k])
    retrieved_relevant = retrieved_ids.intersection(relevant_ids)

    return len(retrieved_relevant) / len(relevant_ids)


def reciprocal_rank_at_k(
    ranked_document_ids: list[str],
    relevant_documents: dict[str, int],
    k: int,
) -> float:
    relevant_ids = {
        document_id
        for document_id, relevance in relevant_documents.items()
        if relevance > 0
    }

    for rank, document_id in enumerate(
        ranked_document_ids[:k],
        start=1,
    ):
        if document_id in relevant_ids:
            return 1.0 / rank

    return 0.0


def ndcg_at_k(
    ranked_document_ids: list[str],
    relevant_documents: dict[str, int],
    k: int,
) -> float:
    positive_relevance = {
        document_id: relevance
        for document_id, relevance in relevant_documents.items()
        if relevance > 0
    }

    retrieved_grades = [
        positive_relevance.get(document_id, 0)
        for document_id in ranked_document_ids[:k]
    ]

    ideal_grades = sorted(
        positive_relevance.values(),
        reverse=True,
    )[:k]

    def dcg(grades: list[int]) -> float:
        return sum(
            (2**grade - 1) / math.log2(rank + 1)
            for rank, grade in enumerate(grades, start=1)
        )

    actual_dcg = dcg(retrieved_grades)
    ideal_dcg = dcg(ideal_grades)

    if ideal_dcg == 0:
        return 0.0

    return actual_dcg / ideal_dcg


def evaluate(
    retriever: Retriever,
    queries: dict[str, str],
    qrels: dict[str, dict[str, int]],
    k: int = 10,
) -> dict[str, float | int]:
    recall_scores = []
    reciprocal_ranks = []
    ndcg_scores = []
    latencies_ms = []

    for query_id, relevant_documents in qrels.items():
        query = queries.get(query_id)

        if query is None:
            continue

        start_time = time.perf_counter()
        results = retriever.search(query, top_k=k)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        ranked_ids = [
            result.document.id
            for result in results
        ]

        recall_scores.append(
            recall_at_k(ranked_ids, relevant_documents, k)
        )
        reciprocal_ranks.append(
            reciprocal_rank_at_k(ranked_ids, relevant_documents, k)
        )
        ndcg_scores.append(
            ndcg_at_k(ranked_ids, relevant_documents, k)
        )
        latencies_ms.append(elapsed_ms)

    query_count = len(recall_scores)

    if query_count == 0:
        raise ValueError("No queries were evaluated.")

    return {
        "evaluated_queries": query_count,
        f"recall@{k}": sum(recall_scores) / query_count,
        f"mrr@{k}": sum(reciprocal_ranks) / query_count,
        f"ndcg@{k}": sum(ndcg_scores) / query_count,
        "average_latency_ms": sum(latencies_ms) / query_count,
    }
    