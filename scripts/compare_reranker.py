import argparse
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
from src.hybrid_retriever import HybridRetriever
from src.reranker import CrossEncoderReranker


DATASET_PATH = Path("data/scifact")
ARTIFACT_PATH = Path("artifacts/dense")
RESULTS_PATH = Path("results")


def print_metrics(
    pipeline: str,
    metrics: dict[str, float | int],
) -> None:
    print(
        f"{pipeline:<22}"
        f"{metrics['recall@10']:>12.4f}"
        f"{metrics['mrr@10']:>12.4f}"
        f"{metrics['ndcg@10']:>12.4f}"
        f"{metrics['average_latency_ms']:>14.2f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--hybrid-candidate-k",
        type=int,
        default=30,
        help=(
            "Candidate depth selected during Day 3"
        ),
    )

    parser.add_argument(
        "--rerank-k",
        type=int,
        default=20,
        help="Hybrid candidates scored by cross-encoder",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
    )

    args = parser.parse_args()

    if args.rerank_k < 10:
        raise ValueError(
            "rerank-k must be at least 10."
        )

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

    hybrid_retriever = HybridRetriever(
        bm25_retriever=bm25_retriever,
        dense_retriever=dense_retriever,
        candidate_k=args.hybrid_candidate_k,
        rrf_k=60,
    )

    print("Loading cross-encoder reranker...")
    reranked_retriever = CrossEncoderReranker(
        candidate_retriever=hybrid_retriever,
        candidate_k=args.rerank_k,
        batch_size=args.batch_size,
    )

    print("Warming up neural models...")
    dense_retriever.search(
        "scientific evidence",
        top_k=1,
    )
    reranked_retriever.warm_up()

    pipelines = {
        "bm25": bm25_retriever,
        "dense": dense_retriever,
        "hybrid": hybrid_retriever,
        "hybrid_reranker": reranked_retriever,
    }

    metrics_by_pipeline = {}

    for pipeline_name, retriever in pipelines.items():
        print(f"\nEvaluating {pipeline_name}...")

        metrics_by_pipeline[pipeline_name] = evaluate(
            retriever=retriever,
            queries=queries,
            qrels=qrels,
            k=10,
        )

    output = {
        "configuration": {
            "test_queries": len(qrels),
            "final_k": 10,
            "hybrid_candidate_k": (
                args.hybrid_candidate_k
            ),
            "rrf_k": 60,
            "rerank_k": args.rerank_k,
            "reranker_batch_size": args.batch_size,
            "reranker_model": (
                "cross-encoder/"
                "ms-marco-MiniLM-L6-v2"
            ),
        },
        "metrics": metrics_by_pipeline,
    }

    RESULTS_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        RESULTS_PATH
        / "day4_pipeline_comparison.json"
    )

    output_path.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print(
        "\n"
        f"{'Pipeline':<22}"
        f"{'Recall@10':>12}"
        f"{'MRR@10':>12}"
        f"{'nDCG@10':>12}"
        f"{'Latency ms':>14}"
    )

    for pipeline, metrics in metrics_by_pipeline.items():
        print_metrics(pipeline, metrics)

    print(f"\nSaved results to {output_path}")


if __name__ == "__main__":
    main()
