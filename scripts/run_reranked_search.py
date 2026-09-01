import argparse
import time
from pathlib import Path

from src.bm25_retriever import BM25Retriever
from src.data_loader import load_corpus
from src.dense_retriever import DenseRetriever
from src.hybrid_retriever import HybridRetriever
from src.reranker import CrossEncoderReranker


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
        "--hybrid-candidate-k",
        type=int,
        default=30,
        help=(
            "Candidates retrieved from BM25 and dense "
            "before RRF"
        ),
    )

    parser.add_argument(
        "--rerank-k",
        type=int,
        default=20,
        help="Hybrid candidates scored by the reranker",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
    )

    args = parser.parse_args()

    documents = load_corpus(
        DATASET_PATH / "corpus.jsonl"
    )

    print(f"Loaded {len(documents)} documents")

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
        candidate_k=args.hybrid_candidate_k,
        rrf_k=60,
    )

    print("Loading cross-encoder...")
    reranker = CrossEncoderReranker(
        candidate_retriever=hybrid_retriever,
        candidate_k=args.rerank_k,
        batch_size=args.batch_size,
    )

    # Exclude one-time initialization from search latency.
    dense_retriever.search(
        "scientific evidence",
        top_k=1,
    )
    reranker.warm_up()

    start_time = time.perf_counter()

    results = reranker.search(
        args.query,
        top_k=args.top_k,
    )

    elapsed_ms = (
        time.perf_counter() - start_time
    ) * 1000

    print(f"\nTotal online latency: {elapsed_ms:.2f} ms")
    print(
        f"Reranked {args.rerank_k} hybrid candidates "
        f"into {len(results)} results"
    )

    for result in results:
        document = result.document
        excerpt = document.text[:250].replace("\n", " ")

        print(f"\nRank: {result.rank}")
        print(f"Document ID: {document.id}")
        print(
            f"Cross-encoder score: "
            f"{result.score:.6f}"
        )
        print(f"Title: {document.title}")
        print(f"Excerpt: {excerpt}...")


if __name__ == "__main__":
    main()
