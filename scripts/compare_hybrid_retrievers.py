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


DATASET_PATH = Path("data/scifact")
ARTIFACT_PATH = Path("artifacts/dense")
RESULTS_PATH = Path("results")
RRF_K = 60


def print_metrics(
    pipeline: str,
    metrics: dict[str, float | int],
) -> None:
    print(
        f"{pipeline:<20}"
        f"{metrics['recall@10']:>12.4f}"
        f"{metrics['mrr@10']:>12.4f}"
        f"{metrics['ndcg@10']:>12.4f}"
        f"{metrics['average_latency_ms']:>14.2f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--split",
        choices=("train", "test"),
        default="test",
        help="Qrels split used for evaluation",
    )

    parser.add_argument(
        "--candidate-depths",
        type=int,
        nargs="+",
        default=[20, 30, 50],
        help="Candidate depths to evaluate",
    )

    args = parser.parse_args()

    if any(depth <= 0 for depth in args.candidate_depths):
        raise ValueError(
            "All candidate depths must be positive."
        )

    documents = load_corpus(
        DATASET_PATH / "corpus.jsonl"
    )

    queries = load_queries(
        DATASET_PATH / "queries.jsonl"
    )

    qrels = load_qrels(
        DATASET_PATH / f"qrels/{args.split}.tsv"
    )

    print(f"Loaded {len(documents)} documents")
    print(
        f"Evaluating {len(qrels)} queries "
        f"from the {args.split} split"
    )

    print("\nBuilding BM25 retriever...")
    bm25_retriever = BM25Retriever(documents)

    print("Loading dense retriever...")
    dense_retriever = DenseRetriever.load(
        documents=documents,
        index_path=ARTIFACT_PATH / "index.faiss",
        metadata_path=ARTIFACT_PATH / "metadata.json",
    )

    # Warm up the embedding model before measuring latency.
    dense_retriever.search(
        "scientific evidence",
        top_k=1,
    )

    metrics_by_pipeline = {}

    print("\nEvaluating BM25...")
    metrics_by_pipeline["bm25"] = evaluate(
        retriever=bm25_retriever,
        queries=queries,
        qrels=qrels,
        k=10,
    )

    print("Evaluating dense retrieval...")
    metrics_by_pipeline["dense"] = evaluate(
        retriever=dense_retriever,
        queries=queries,
        qrels=qrels,
        k=10,
    )

    for candidate_depth in args.candidate_depths:
        pipeline_name = (
            f"hybrid_rrf_{candidate_depth}"
        )

        print(
            "\nEvaluating hybrid retrieval with "
            f"candidate depth {candidate_depth}..."
        )

        hybrid_retriever = HybridRetriever(
            bm25_retriever=bm25_retriever,
            dense_retriever=dense_retriever,
            candidate_k=candidate_depth,
            rrf_k=RRF_K,
        )

        metrics_by_pipeline[pipeline_name] = evaluate(
            retriever=hybrid_retriever,
            queries=queries,
            qrels=qrels,
            k=10,
        )

    output = {
        "configuration": {
            "split": args.split,
            "final_k": 10,
            "rrf_k": RRF_K,
            "candidate_depths": args.candidate_depths,
        },
        "metrics": metrics_by_pipeline,
    }

    RESULTS_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        RESULTS_PATH
        / f"day3_{args.split}_comparison.json"
    )

    output_path.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print(
        "\n"
        f"{'Pipeline':<20}"
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
