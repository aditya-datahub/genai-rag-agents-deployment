# Capstone 3 — AstraRAG (Agentic RAG Chatbot, Production-Grade)

The most advanced capstone: a RAG chatbot wrapped in an **agent**, so it can
decide when to retrieve, when to use other tools, and how to combine results
— rather than always following the same fixed retrieve-then-generate flow.
Deployed both locally with Docker and to AWS EC2 with Docker.

## What it covers
- Environment setup and a document ingestion pipeline (Module 5 concepts).
- Building the RAG **agent** itself — combining retrieval as one of several
  tools available to an agent (Module 6 concepts), rather than a fixed
  pipeline.
- A full backend + frontend application around the agent.
- Two deployment paths: local Docker (for dev/testing) and Docker on AWS EC2
  (for production), per Module 7.

## Why "agentic RAG"?
A fixed RAG pipeline always retrieves before answering, even for questions
that don't need it (e.g. "hi, how are you?"), and can't combine retrieval
with other actions. An agentic RAG system treats retrieval as *one tool among
several*, so the agent can decide per-query whether to retrieve, use another
tool, or answer directly — closer to how a production support/assistant bot
actually needs to behave.

## Suggested structure
```
astrarag/
├── backend/
│   ├── ingest.py
│   ├── agent.py          # agent with retrieval as a tool
│   └── api.py            # FastAPI backend
├── frontend/
│   └── app.py            # chat UI
├── docker-compose.yml    # local multi-container setup
├── Dockerfile
└── requirements.txt
```

> Fill this in with your actual implementation from the course project.
