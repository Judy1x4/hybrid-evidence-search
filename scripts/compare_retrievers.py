import json
from pathlib import Path

from src.bm25_retriever import BM25Retriever
from src.data_loader import (
    load_corpus,
    load_qrels,
    load_queries,
)
from src.dense_retriever import DenseRetriever
from src.evaluation import evaluate


DATASET_PATH = Path("data/scifact")
ARTIFACT_PATH = Path("artifacts/dense")
RESULTS_PATH = Path("results")


def main() -> None:
    documents = load_corpus(
        DATASET_PATH / "corpus.jsonl"
    )

    queries = load_queries(
        DATASET_PATH / "queries.jsonl"
    )

    qrels = load_qrels(
        DATASET_PATH / "qrels/test.tsv"
    )

    print(f"Loaded {len(documents)} documents")
    print(f"Evaluating {len(qrels)} test queries")

    print("\nBuilding BM25 retriever...")
    bm25_retriever = BM25Retriever(documents)

    print("Loading dense retriever...")
    dense_retriever = DenseRetriever.load(
        documents=documents,
        index_path=ARTIFACT_PATH / "index.faiss",
        metadata_path=ARTIFACT_PATH / "metadata.json",
    )

    # Warm up both retrievers before measuring latency.
    first_query_id = next(iter(qrels))
    warmup_query = queries[first_query_id]

    bm25_retriever.search(warmup_query, top_k=10)
    dense_retriever.search(warmup_query, top_k=10)

    print("\nEvaluating BM25...")
    bm25_metrics = evaluate(
        retriever=bm25_retriever,
        queries=queries,
        qrels=qrels,
        k=10,
    )

    print("Evaluating dense retrieval...")
    dense_metrics = evaluate(
        retriever=dense_retriever,
        queries=queries,
        qrels=qrels,
        k=10,
    )

    comparison = {
        "bm25": bm25_metrics,
        "dense": dense_metrics,
    }

    RESULTS_PATH.mkdir(exist_ok=True)

    output_path = (
        RESULTS_PATH / "retrieval_comparison.json"
    )

    output_path.write_text(
        json.dumps(comparison, indent=2),
        encoding="utf-8",
    )

    print("\nResults")
    print(
        f"{'Pipeline':<12}"
        f"{'Recall@10':>12}"
        f"{'MRR@10':>12}"
        f"{'nDCG@10':>12}"
        f"{'Latency':>14}"
    )

    for pipeline_name, metrics in comparison.items():
        print(
            f"{pipeline_name:<12}"
            f"{metrics['recall@10']:>12.4f}"
            f"{metrics['mrr@10']:>12.4f}"
            f"{metrics['ndcg@10']:>12.4f}"
            f"{metrics['average_latency_ms']:>11.2f} ms"
        )

    print(f"\nSaved comparison to {output_path}")


if __name__ == "__main__":
    main()
