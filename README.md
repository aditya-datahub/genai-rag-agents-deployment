<div align="center">

# 🤖 From "What is a Transformer?" to Deploying AI Agents on AWS

### *A 23-hour deep dive into Generative AI — documented, coded, and shipped.*

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-1C3C3C)](https://python.langchain.com/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-🦙-4B0082)](https://www.llamaindex.ai/)
[![FastAPI](https://img.shields.io/badge/FastAPI-⚡-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-🐳-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-☁️-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

**📄 [Certificate](./assets/certificate.pdf)** &nbsp;•&nbsp; **🔗 [Verify it's real](ude.my/UC-2f827bf7-355e-4afe-8333-224ada998cd4)**

</div>

<br>

## 👋 So, what's the story here?

A few weeks ago this repo didn't exist. Neither did any real understanding of
why a chatbot suddenly "knows" your PDF, or how an AI agent decides which
tool to pick, or what actually happens when you type `docker run` and an LLM
starts answering questions on a server somewhere in `us-east-1`.

23 hours, 70 lectures, and a *lot* of `pip install` errors later — here's the
proof of work as a student who took the course (not an instructor — that
credit goes to Siddhardhan S and Aditya Sharma). Every folder below is a
rabbit hole I went down, survived, and turned into something that actually
runs.

If you're learning this stuff too: clone it, break it, rebuild it. That's
kind of the whole point.

<br>

## 🗺️ The Journey (a.k.a. Repo Structure)

| Stage | Module | What happens here |
|:---:|---|---|
| 🌱 | [`01-genai-foundations`](./01-genai-foundations) | Where "AI" stops being a buzzword — LLMs, Transformers, attention, demystified |
| 🔌 | [`02-accessing-llms`](./02-accessing-llms) | Talking to OpenAI, Gemini, Groq & Ollama without writing the same code 4 times |
| ✍️ | [`03-prompt-engineering`](./03-prompt-engineering) | The art of asking nicely — zero-shot vs few-shot, side by side |
| 💬 | [`04-genai-chatbots`](./04-genai-chatbots) | Giving the LLM a memory and a face (Streamlit UI included) |
| 📚 | [`05-rag`](./05-rag) | Teaching an LLM to answer from *your* documents, not just its training data |
| 🕵️ | [`06-ai-agents`](./06-ai-agents) | LLMs that don't just talk — they *do* things, using PydanticAI, AutoGen & CrewAI |
| 🚀 | [`07-llm-deployment`](./07-llm-deployment) | Taking it off my laptop — Docker, EC2, vLLM, RunPod |
| 🔗 | [`08-mcp`](./08-mcp) | The protocol that lets any agent use any tool — no more custom glue code |
| 🏆 | [`09-capstone-projects`](./09-capstone-projects) | Three real apps where everything above finally clicks together |

Every module has a `notes.md` (the "wait, why does this work?" answers) and
actual runnable code — not just theory.

<details>
<summary>📁 Prefer a literal file tree? Click here.</summary>

```
genai-rag-agents-deployment/
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
├── .gitignore
│
├── 01-genai-foundations/
│   └── notes.md
│
├── 02-accessing-llms/
│   ├── notes.md
│   └── access_llms_example.py
│
├── 03-prompt-engineering/
│   ├── notes.md
│   └── prompt_templates.py
│
├── 04-genai-chatbots/
│   ├── notes.md
│   └── chatbot_streamlit.py
│
├── 05-rag/
│   ├── notes.md
│   └── rag_pipeline_langchain.py
│
├── 06-ai-agents/
│   ├── notes.md
│   └── agent_example.py
│
├── 07-llm-deployment/
│   ├── notes.md
│   ├── deploy_fastapi.py
│   └── Dockerfile
│
├── 08-mcp/
│   ├── notes.md
│   └── mcp_server_example.py
│
├── 09-capstone-projects/
│   ├── convopro/
│   │   └── README.md
│   ├── studypal/
│   │   └── README.md
│   └── astrarag/
│       └── README.md
│
└── assets/
    └── certificate/
        └── certificate.pdf
```

</details>

<br>

## 🧰 What's Under the Hood

<div align="center">

| 🧠 Brains | 🕵️ Agents | 🗃️ Memory | 🎨 Face | 🚀 Ships It |
|:---:|:---:|:---:|:---:|:---:|
| LangChain | PydanticAI | Chroma | Streamlit | Docker |
| LlamaIndex | AutoGen | — | — | AWS EC2 |
| — | CrewAI | — | — | vLLM / RunPod |

</div>

<br>

## ⚡ Try It Yourself

```bash
git clone https://github.com/<your-username>/genai-rag-agents-deployment.git
cd genai-rag-agents-deployment

python -m venv venv && source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # drop your API key in here
```

Then pick a rabbit hole:

```bash
python 05-rag/rag_pipeline_langchain.py        # ask questions, get grounded answers
python 06-ai-agents/agent_example.py           # watch an agent reason step by step
streamlit run 04-genai-chatbots/chatbot_streamlit.py   # chat with memory, in the browser
uvicorn 07-llm-deployment.deploy_fastapi:app --reload  # your own AI, as an API
```

<br>

## 🏆 The Capstones — Where It All Comes Together

| Project | The Pitch |
|---|---|
| 💬 [**ConvoPro**](./09-capstone-projects/convopro) | Your own private ChatGPT — no OpenAI dashboard, no data leaving your server |
| 📖 [**StudyPal**](./09-capstone-projects/studypal) | Dump your notes in, ask it anything — an AI that actually studied *your* syllabus |
| 🤖 [**AstraRAG**](./09-capstone-projects/astrarag) | The final boss: an agent that knows *when* to search your docs, not just how |

<br>

## 🎓 Proof It Happened

| | |
|---|---|
| **Course** | Complete Generative AI Course: RAG, AI Agents & Deployment |
| **Instructors** | Siddhardhan S|
| **Completed by** | *Aditya Sharma* |
| **Completed on** | September 8, 2026 |
| **Damage** | 23 hours · 70 lectures · more coffee than I'd like to admit |

📄 [Certificate PDF](./assets/certificate.pdf) &nbsp;•&nbsp; 🔗 [Verify Online](ude.my/UC-2f827bf7-355e-4afe-8333-224ada998cd4)

<br>

## 📜 License

MIT — see [LICENSE](./LICENSE). Fork it, remix it, learn from it. That's the deal.

---

<div align="center">

**If this saved you an hour of Googling "why does my RAG pipeline hallucinate," drop a ⭐.**

*Built one confused `print()` statement at a time.*

</div>
