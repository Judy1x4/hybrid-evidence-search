Project: Hybrid Evidence Search Engine
Build a search engine that retrieves relevant documents for natural-language queries and compares four approaches:
BM25 keyword retrieval
Dense embedding retrieval
Hybrid retrieval
Hybrid retrieval with cross-encoder reranking
Use the BEIR SciFact dataset because it already provides documents, queries, and relevance labels. That saves you from spending half the week collecting and labelling data.
Core architecture
flowchart TD
    A["User query"] --> B["BM25 retrieval"]
    A --> C["Dense retrieval"]
    B --> D["Hybrid fusion"]
    C --> D
    D --> E["Cross-encoder reranking"]
    E --> F["Ranked documents"]

Recommended stack
Python
Sentence Transformers
FAISS
BM25
Cross-encoder reranker
FastAPI
React
pytest
Optional LLM API for answer generation
One-week schedule
Assuming approximately 4–6 focused hours each day:
Day 1 — Dataset and BM25 baseline
Learn:
Document retrieval basics
Inverted indexes and BM25
Queries, documents, relevance labels
Recall@K, MRR and nDCG
Build:
Load the SciFact corpus, queries, and relevance labels
Create a common Document data structure
Implement BM25 retrieval
Return the top 10 results with scores
Create the initial evaluation script
End-of-day target: BM25 results and baseline metrics.
Day 2 — Dense retrieval
Learn:
Text embeddings
Cosine similarity
Bi-encoder retrieval
Vector indexes
Build:
Encode all documents with a pretrained sentence-transformer
Store embeddings in FAISS
Encode incoming queries
Retrieve the top 10 semantically similar documents
Compare dense retrieval against BM25
End-of-day target: two independently evaluated retrieval systems.
Day 3 — Hybrid retrieval
Learn:
Why sparse and dense retrieval make different mistakes
Rank fusion
Reciprocal Rank Fusion
Build:
Retrieve candidates from both BM25 and FAISS
Combine rankings using Reciprocal Rank Fusion
Experiment with retrieving 20–50 candidates from each system
Evaluate BM25, dense, and hybrid retrieval consistently
End-of-day target: a hybrid search pipeline with measurable results.
Day 4 — Cross-encoder reranking
Learn:
Bi-encoder versus cross-encoder models
Candidate generation versus reranking
Quality and latency trade-offs
Build:
Take the top 20 hybrid candidates
Score each query-document pair using a cross-encoder
Return the reranked top 10
Measure both retrieval quality and latency
Your final results table should resemble:
Pipeline
Recall@10
MRR@10
nDCG@10
Avg. latency
BM25
—
—
—
—
Dense
—
—
—
—
Hybrid
—
—
—
—
Hybrid + reranker
—
—
—
—

End-of-day target: complete AI/search functionality.
Day 5 — Error analysis and API
Build:
FastAPI search endpoint
Pipeline-selection parameter
Structured result objects
Model and index caching
Input validation
Unit tests for retrieval and ranking
Analyze at least 10 queries:
Where did BM25 outperform dense retrieval?
Where did dense retrieval understand semantic similarity?
Did reranking improve every query?
Which queries still failed, and why?
How much latency did reranking add?
The error analysis is important—it demonstrates actual understanding beyond using libraries.
Day 6 — Minimal frontend and optional RAG
Build a small React interface containing:
Query input
Pipeline selector
Ranked search results
Scores and document excerpts
Search latency
Comparison view between two pipelines
If everything else is complete, add an optional grounded answer:
Retrieved documents
        ↓
LLM prompt
        ↓
Answer with document citations

Do not prioritize RAG over evaluation. The search system is the project; answer generation is only an extension.
Day 7 — Portfolio preparation
Finish:
Refactor and clean the repository
Add tests and setup instructions
Produce the final evaluation table
Add an architecture diagram
Document three successful and three failed queries
Explain design decisions and limitations
Record a 60–90 second demonstration
Deploy only if it can be done quickly
Repository structure
hybrid-evidence-search/
├── backend/
│   ├── api.py
│   └── schemas.py
├── frontend/
├── src/
│   ├── data_loader.py
│   ├── bm25_retriever.py
│   ├── dense_retriever.py
│   ├── hybrid_retriever.py
│   ├── reranker.py
│   └── evaluation.py
├── tests/
├── scripts/
│   ├── build_index.py
│   └── run_evaluation.py
├── results/
│   └── metrics.json
├── requirements.txt
└── README.md

Definition of done
By the end of the week, the project should have:
Four working and comparable search pipelines
Reproducible evaluation results
Latency measurements
A concise error analysis
A working API
A simple frontend demonstration
Clear documentation and tests
Avoid adding agents, multimodal search, RLHF, authentication, user accounts, databases, or a complicated UI. Those would dilute the part you are trying to learn and demonstrate.
A future résumé bullet could be:
Developed and evaluated a hybrid neural search engine combining BM25, dense vector retrieval, reciprocal rank fusion, and cross-encoder reranking; measured retrieval quality using Recall@K, MRR, and nDCG and exposed the pipeline through FastAPI and React.
This is realistic for one intensive week and directly relevant to TikTok Search without pretending to cover the entire role.













