"""
FastAPI service that exposes the RAG pipeline from Module 5 as an HTTP API.

Run locally (from the repo root, so the module import below resolves):
    uvicorn 07-llm-deployment.deploy_fastapi:app --reload

Then POST to /ask:
    curl -X POST http://127.0.0.1:8000/ask \
         -H "Content-Type: application/json" \
         -d '{"question": "What is RAG?"}'
"""

import os
import sys

# Allow importing the Module 5 pipeline when run from the repo root.
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "05-rag"))

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from rag_pipeline_langchain import (  # noqa: E402
    build_sample_doc_if_missing,
    load_and_split,
    build_vectorstore,
    build_rag_chain,
    SAMPLE_DOC_PATH,
)

load_dotenv()

app = FastAPI(title="GenAI RAG Service", version="1.0.0")

# Build the chain once at startup, not per-request.
_chain = None


@app.on_event("startup")
def startup():
    global _chain
    build_sample_doc_if_missing()
    chunks = load_and_split(SAMPLE_DOC_PATH)
    vectorstore = build_vectorstore(chunks)
    _chain = build_rag_chain(vectorstore)


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    question: str
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    answer = _chain.invoke(request.question)
    return AskResponse(question=request.question, answer=answer)
