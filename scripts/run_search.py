import argparse
from pathlib import Path

from src.bm25_retriever import BM25Retriever
from src.data_loader import load_corpus


DATASET_PATH = Path("data/scifact")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Scientific claim or search query")
    parser.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()

    documents = load_corpus(DATASET_PATH / "corpus.jsonl")
    retriever = BM25Retriever(documents)

    results = retriever.search(args.query, top_k=args.top_k)

    for result in results:
        document = result.document
        excerpt = document.text[:250].replace("\n", " ")

        print(f"\nRank: {result.rank}")
        print(f"Document ID: {document.id}")
        print(f"Score: {result.score:.4f}")
        print(f"Title: {document.title}")
        print(f"Excerpt: {excerpt}...")


if __name__ == "__main__":
    main()
