<div align="center">

# 🤖 Complete Generative AI — RAG, AI Agents & Deployment

**Hands-on notes and projects from a 23-hour, 70-lecture Generative AI course** — from Transformer fundamentals to building and deploying agentic RAG systems in the cloud.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?logo=langchain&logoColor=white)](https://python.langchain.com/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-Data%20Framework-4B0082)](https://www.llamaindex.ai/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Serving-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-EC2%20Deploy-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

📄 [Certificate PDF](./assets/certificate/certificate.pdf) &nbsp;·&nbsp; 🔗 [Verify Online](ude.my/UC-2f827bf7-355e-4afe-8333-224ada998cd4)

</div>

---

## 📖 About

This repository documents everything built while completing **"Complete
Generative AI Course: RAG, AI Agents & Deployment"** by **Siddhardhan S** and
**Aditya Sharma** — covering LLM foundations, prompt engineering, chatbots,
Retrieval-Augmented Generation (RAG), multi-agent systems, the Model Context
Protocol (MCP), and real cloud deployment on AWS.

It's organized to mirror the course's own structure, so each folder maps
cleanly to a topic — with concise notes and working, runnable code for every
module, plus three capstone projects tying it all together.

## 📑 Table of Contents

- [Repo Structure](#-repo-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Capstone Projects](#-capstone-projects)
- [Certificate](#-certificate)
- [License](#-license)

## 🗂 Repo Structure

| # | Module | Covers |
|---|---|---|
| 01 | [`genai-foundations`](./01-genai-foundations) | AI vs ML vs DL vs GenAI, Large Language Models, Transformer architecture |
| 02 | [`accessing-llms`](./02-accessing-llms) | OpenAI, Gemini, Groq, Ollama — accessed via LangChain & LlamaIndex |
| 03 | [`prompt-engineering`](./03-prompt-engineering) | Prompt templates, zero-shot vs few-shot prompting |
| 04 | [`genai-chatbots`](./04-genai-chatbots) | Chatbots with LangChain/LlamaIndex, Streamlit UI, Streamlit Cloud deploy |
| 05 | [`rag`](./05-rag) | RAG pipelines with LangChain & LlamaIndex, PDF Q&A app |
| 06 | [`ai-agents`](./06-ai-agents) | Tool-using agents, PydanticAI, Microsoft AutoGen, CrewAI multi-agent systems |
| 07 | [`llm-deployment`](./07-llm-deployment) | Ollama + Docker, AWS EC2, vLLM, RunPod, FastAPI serving |
| 08 | [`mcp`](./08-mcp) | Model Context Protocol server & agent integration |
| 09 | [`capstone-projects`](./09-capstone-projects) | ConvoPro · StudyPal · AstraRAG |

Every module folder contains a `notes.md` (concepts + key takeaways) and
runnable example code where applicable.

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| **Orchestration** | LangChain, LlamaIndex |
| **Agent Frameworks** | PydanticAI, Microsoft AutoGen, CrewAI |
| **Vector Store** | Chroma |
| **UI** | Streamlit |
| **Serving** | FastAPI, Uvicorn, Ollama, vLLM |
| **Infrastructure** | Docker, AWS EC2, RunPod |
| **Protocol** | Model Context Protocol (MCP) |

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/genai-rag-agents-deployment.git
cd genai-rag-agents-deployment

python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows

pip install -r requirements.txt
cp .env.example .env            # add your API key(s)
```

Run modules individually:

```bash
python 02-accessing-llms/access_llms_example.py
python 03-prompt-engineering/prompt_templates.py
streamlit run 04-genai-chatbots/chatbot_streamlit.py
python 05-rag/rag_pipeline_langchain.py
python 06-ai-agents/agent_example.py
uvicorn 07-llm-deployment.deploy_fastapi:app --reload
python 08-mcp/mcp_server_example.py
```

## 🏗 Capstone Projects

| Project | Description |
|---|---|
| [**ConvoPro**](./09-capstone-projects/convopro) | Private, self-hosted ChatGPT-style chatbot, deployed on AWS EC2 |
| [**StudyPal**](./09-capstone-projects/studypal) | RAG-powered AI study assistant that answers questions from your own notes |
| [**AstraRAG**](./09-capstone-projects/astrarag) | Production-grade agentic RAG chatbot with full backend + frontend, deployed with Docker |

## 🎓 Certificate

| | |
|---|---|
| **Course** | Complete Generative AI Course: RAG, AI Agents & Deployment |
| **Instructors** | Siddhardhan S, Aditya Sharma |
| **Completed** | September 8, 2026 |
| **Length** | 23 hours · 70 lectures · 12 sections |

📄 [Certificate PDF](./assets/certificate/certificate.pdf) &nbsp;·&nbsp; 🔗 [Verify Online](ude.my/UC-2f827bf7-355e-4afe-8333-224ada998cd4)

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

<div align="center">

Built while learning Generative AI, one module at a time.
⭐ **Star this repo** if you find it useful!

</div>
