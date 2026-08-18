import argparse
from pathlib import Path

from src.data_loader import load_corpus
from src.dense_retriever import DenseRetriever


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
    )

    args = parser.parse_args()

    documents = load_corpus(
        DATASET_PATH / "corpus.jsonl"
    )

    retriever = DenseRetriever.load(
        documents=documents,
        index_path=ARTIFACT_PATH / "index.faiss",
        metadata_path=ARTIFACT_PATH / "metadata.json",
    )

    results = retriever.search(
        args.query,
        top_k=args.top_k,
    )

    for result in results:
        document = result.document
        excerpt = document.text[:250].replace("\n", " ")

        print(f"\nRank: {result.rank}")
        print(f"Document ID: {document.id}")
        print(f"Cosine similarity: {result.score:.4f}")
        print(f"Title: {document.title}")
        print(f"Excerpt: {excerpt}...")


if __name__ == "__main__":
    main()
