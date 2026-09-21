# Capstone 2 — StudyPal (RAG-Powered AI Study Assistant)

A study assistant that ingests your own documents (lecture notes, textbooks,
slides) and answers questions grounded in that material, using the RAG
pipeline from Module 5.

## What it covers
- Environment setup and document ingestion pipeline (loading + chunking user
  study material).
- Full RAG pipeline implementation (embed → store → retrieve → generate),
  applied specifically to study Q&A rather than the generic demo doc in
  `05-rag/`.
- Deployment to AWS EC2, building on Module 7.

## Why it matters
Shows RAG applied to a concrete, personally useful use case end-to-end:
ingest → index → query → deploy, rather than just the pipeline in isolation.

## Suggested structure
```
studypal/
├── ingest.py             # document ingestion pipeline
├── rag_engine.py         # retrieval + generation logic
├── app.py                # UI (Streamlit or FastAPI)
├── Dockerfile
└── requirements.txt
```

> Fill this in with your actual implementation from the course project.
