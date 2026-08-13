import csv
import json
from collections import defaultdict
from pathlib import Path

from src.models import Document


def load_corpus(path: Path) -> list[Document]:
    documents = []

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)

            documents.append(
                Document(
                    id=str(record["_id"]),
                    title=record.get("title", ""),
                    text=record["text"],
                )
            )

    return documents


def load_queries(path: Path) -> dict[str, str]:
    queries = {}

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            record = json.loads(line)
            queries[str(record["_id"])] = record["text"]

    return queries


def load_qrels(path: Path) -> dict[str, dict[str, int]]:
    qrels = defaultdict(dict)

    with path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")

        for row in reader:
            query_id = str(row["query-id"])
            document_id = str(row["corpus-id"])
            relevance = int(row["score"])

            qrels[query_id][document_id] = relevance

    return dict(qrels)
