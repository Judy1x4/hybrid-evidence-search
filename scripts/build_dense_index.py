import json
import time
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from src.data_loader import load_corpus


DATASET_PATH = Path("data/scifact")
ARTIFACT_PATH = Path("artifacts/dense")

MODEL_NAME = "sentence-transformers/msmarco-MiniLM-L6-cos-v5"
BATCH_SIZE = 64


def main() -> None:
    documents = load_corpus(DATASET_PATH / "corpus.jsonl")

    print(f"Loaded {len(documents)} documents")
    print(f"Loading embedding model: {MODEL_NAME}")

    model = SentenceTransformer(MODEL_NAME)

    searchable_texts = [
        document.searchable_text
        for document in documents
    ]

    print("Encoding documents...")
    start_time = time.perf_counter()

    embeddings = model.encode_document(
        searchable_texts,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    elapsed_seconds = time.perf_counter() - start_time

    # FAISS expects contiguous float32 arrays.
    embeddings = np.ascontiguousarray(
        embeddings,
        dtype=np.float32,
    )

    document_count, embedding_dimension = embeddings.shape

    if document_count != len(documents):
        raise ValueError(
            "The number of embeddings does not match "
            "the number of documents."
        )

    norms = np.linalg.norm(embeddings, axis=1)

    if not np.allclose(norms, 1.0, atol=1e-3):
        raise ValueError("Document embeddings are not normalized.")

    print(f"Embedding shape: {embeddings.shape}")
    print(f"Encoding time: {elapsed_seconds:.2f} seconds")

    # Inner product between normalized vectors equals cosine similarity.
    index = faiss.IndexFlatIP(embedding_dimension)
    index.add(embeddings)

    if index.ntotal != len(documents):
        raise ValueError("Not all document embeddings were indexed.")

    ARTIFACT_PATH.mkdir(parents=True, exist_ok=True)

    index_path = ARTIFACT_PATH / "index.faiss"
    metadata_path = ARTIFACT_PATH / "metadata.json"

    faiss.write_index(index, str(index_path))

    metadata = {
        "model_name": MODEL_NAME,
        "embedding_dimension": embedding_dimension,
        "document_count": len(documents),
        "document_ids": [
            document.id
            for document in documents
        ],
        "document_encoding_seconds": elapsed_seconds,
    }

    metadata_path.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(f"Stored {index.ntotal} vectors")
    print(f"Saved FAISS index to {index_path}")
    print(f"Saved metadata to {metadata_path}")


if __name__ == "__main__":
    main()
