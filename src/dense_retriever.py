import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from src.models import Document, SearchResult


class DenseRetriever:
    def __init__(
        self,
        documents: list[Document],
        index: faiss.Index,
        model_name: str,
    ) -> None:
        if not documents:
            raise ValueError(
                "Cannot create a dense retriever without documents."
            )

        if index.ntotal != len(documents):
            raise ValueError(
                "FAISS index size does not match document count."
            )

        self.documents = documents
        self.index = index
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

        model_dimension = self.model.get_sentence_embedding_dimension()

        if model_dimension != self.index.d:
            raise ValueError(
                "Embedding model dimension does not match "
                "the FAISS index dimension."
            )

    @classmethod
    def load(
        cls,
        documents: list[Document],
        index_path: Path,
        metadata_path: Path,
    ) -> "DenseRetriever":
        metadata = json.loads(
            metadata_path.read_text(encoding="utf-8")
        )

        document_by_id = {
            document.id: document
            for document in documents
        }

        ordered_documents = []

        for document_id in metadata["document_ids"]:
            document = document_by_id.get(document_id)

            if document is None:
                raise ValueError(
                    f"Indexed document {document_id} "
                    "is missing from the corpus."
                )

            ordered_documents.append(document)

        if len(ordered_documents) != len(documents):
            raise ValueError(
                "Metadata document count does not match the corpus."
            )

        index = faiss.read_index(str(index_path))

        return cls(
            documents=ordered_documents,
            index=index,
            model_name=metadata["model_name"],
        )

    def search(
        self,
        query: str,
        top_k: int = 10,
    ) -> list[SearchResult]:
        if not query.strip() or top_k <= 0:
            return []

        top_k = min(top_k, self.index.ntotal)

        query_embedding = self.model.encode_query(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        query_embedding = np.ascontiguousarray(
            query_embedding,
            dtype=np.float32,
        )

        if query_embedding.shape[1] != self.index.d:
            raise ValueError(
                "Query embedding dimension does not match the index."
            )

        scores, indices = self.index.search(
            query_embedding,
            top_k,
        )

        results = []

        for rank, (score, index_position) in enumerate(
            zip(scores[0], indices[0]),
            start=1,
        ):
            # FAISS can return -1 if it cannot produce enough results.
            if index_position == -1:
                continue

            results.append(
                SearchResult(
                    document=self.documents[int(index_position)],
                    score=float(score),
                    rank=rank,
                )
            )

        return results
