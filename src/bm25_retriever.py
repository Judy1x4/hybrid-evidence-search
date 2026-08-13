import numpy as np
from rank_bm25 import BM25Okapi

from src.models import Document, SearchResult
from src.tokenizer import tokenize


class BM25Retriever:
    def __init__(self, documents: list[Document]) -> None:
        if not documents:
            raise ValueError("Cannot build a BM25 index without documents.")

        self.documents = documents

        tokenized_corpus = [
            tokenize(document.searchable_text)
            for document in documents
        ]

        self.index = BM25Okapi(tokenized_corpus)

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        query_tokens = tokenize(query)

        if not query_tokens:
            return []

        scores = self.index.get_scores(query_tokens)
        top_k = min(top_k, len(self.documents))

        ranked_indices = np.argsort(scores)[::-1][:top_k]

        return [
            SearchResult(
                document=self.documents[document_index],
                score=float(scores[document_index]),
                rank=rank,
            )
            for rank, document_index in enumerate(ranked_indices, start=1)
        ]
