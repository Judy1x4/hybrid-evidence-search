import argparse
from pathlib import Path

from src.bm25_retriever import BM25Retriever
from src.data_loader import load_corpus
from src.dense_retriever import DenseRetriever
from src.hybrid_retriever import HybridRetriever


DATASET_PATH = Path("data/scifact")
ARTIFACT_PATH = Path("artifacts/dense")


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "query",
        help="Scientific claim or natural-language query",
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Number of final results",
    )

    parser.add_argument(
        "--candidate-k",
        type=int,
        default=30,
        help="Candidates retrieved from each system",
    )

    parser.add_argument(
        "--rrf-k",
        type=int,
        default=60,
        help="RRF ranking constant",
    )

    args = parser.parse_args()

    documents = load_corpus(
        DATASET_PATH / "corpus.jsonl"
    )

    print("Building BM25 retriever...")
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
        candidate_k=args.candidate_k,
        rrf_k=args.rrf_k,
    )

    results = hybrid_retriever.search(
        args.query,
        top_k=args.top_k,
    )

    print(
        f"\nCandidate depth per system: "
        f"{args.candidate_k}"
    )

    for result in results:
        document = result.document
        excerpt = document.text[:250].replace("\n", " ")

        print(f"\nRank: {result.rank}")
        print(f"Document ID: {document.id}")
        print(f"RRF score: {result.score:.6f}")
        print(f"Title: {document.title}")
        print(f"Excerpt: {excerpt}...")


if __name__ == "__main__":
    main()
