import json
from pathlib import Path

from src.bm25_retriever import BM25Retriever
from src.data_loader import load_corpus, load_qrels, load_queries
from src.evaluation import evaluate


DATASET_PATH = Path("data/scifact")
RESULTS_PATH = Path("results")


def main() -> None:
    documents = load_corpus(DATASET_PATH / "corpus.jsonl")
    queries = load_queries(DATASET_PATH / "queries.jsonl")
    qrels = load_qrels(DATASET_PATH / "qrels/test.tsv")

    print(f"Loaded {len(documents)} documents")
    print(f"Loaded {len(queries)} total queries")
    print(f"Evaluating {len(qrels)} test queries")
    print("Building BM25 index...")

    retriever = BM25Retriever(documents)

    print("Running evaluation...")
    metrics = evaluate(
        retriever=retriever,
        queries=queries,
        qrels=qrels,
        k=10,
    )

    RESULTS_PATH.mkdir(exist_ok=True)
    output_path = RESULTS_PATH / "bm25_metrics.json"

    output_path.write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(metrics, indent=2))
    print(f"Saved results to {output_path}")


if __name__ == "__main__":
    main()
