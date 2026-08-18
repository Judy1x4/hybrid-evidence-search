# scripts/debug_dense_query.py

import json
from pathlib import Path

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

    print("Loading dense retriever...")
    dense_retriever = DenseRetriever.load(
        documents=documents,
        index_path=ARTIFACT_PATH / "index.faiss",
        metadata_path=ARTIFACT_PATH / "metadata.json",
    )

    query_id = "1"  # Replace with an ID appearing in test.tsv

    if query_id not in queries:
        raise ValueError(f"Query ID {query_id!r} was not found in queries.")

    if query_id not in qrels:
        raise ValueError(
            f"Query ID {query_id!r} has no relevance labels in test.tsv."
        )

    query = queries[query_id]

    relevant_ids = {
        document_id
        for document_id, relevance in qrels[query_id].items()
        if relevance > 0
    }

    results = dense_retriever.search(query, top_k=10)

    print(f"\nQuery ID: {query_id}")
    print(f"Query: {query}")
    print(f"Relevant document IDs: {relevant_ids}\n")

    for result in results:
        document_id = result.document.id
        is_relevant = document_id in relevant_ids

        print(
            f"Rank {result.rank}: "
            f"Document {document_id} | "
            f"Score {result.score:.4f} "
            f"{'RELEVANT' if is_relevant else ''}"
        )


if __name__ == "__main__":
    main()
