from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Document:
    id: str
    title: str
    text: str

    @property
    def searchable_text(self) -> str:
        return f"{self.title} {self.text}".strip()


@dataclass(frozen=True, slots=True)
class SearchResult:
    document: Document
    score: float
    rank: int
