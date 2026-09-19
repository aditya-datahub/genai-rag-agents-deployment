# Capstone 1 — ConvoPro (Private ChatGPT Clone)

A self-hosted, private chatbot application — your own ChatGPT-style interface
that you control end-to-end, deployed on your own infrastructure instead of
relying on a third-party hosted product.

## What it covers
- Database & environment setup for storing conversation history per user.
- Core chatbot implementation (LLM + memory + UI), building on the patterns
  from Module 4 (chatbots) and Module 2 (accessing LLMs).
- Deployment to AWS EC2, building on Module 7 (LLM deployment).

## Why it matters
Demonstrates a full, deployable product rather than an isolated script:
persistence (DB), a real backend/frontend split, and a live cloud deployment
a user could actually reach over the internet.

## Suggested structure
```
convopro/
├── app/
│   ├── main.py          # FastAPI or Streamlit entrypoint
│   ├── db.py            # conversation persistence
│   └── chat.py          # LLM + memory logic
├── Dockerfile
└── requirements.txt
```

> Fill this in with your actual implementation from the course project.
