"""
Demonstrates accessing multiple LLM providers through LangChain's unified
interface. Uncomment/configure the provider you have credentials for.

Usage:
    python access_llms_example.py
"""

import os
from dotenv import load_dotenv

load_dotenv()


def call_openai(prompt: str) -> str:
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    return llm.invoke(prompt).content


def call_groq(prompt: str) -> str:
    # pip install langchain-groq
    from langchain_groq import ChatGroq

    llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0.3)
    return llm.invoke(prompt).content


def call_ollama_local(prompt: str) -> str:
    # Requires Ollama running locally: https://ollama.com
    from langchain_community.chat_models import ChatOllama

    llm = ChatOllama(model="llama3")
    return llm.invoke(prompt).content


PROVIDERS = {
    "openai": call_openai,
    "groq": call_groq,
    "ollama": call_ollama_local,
}


def main():
    provider = os.getenv("LLM_PROVIDER", "openai")
    prompt = "Explain the difference between RAG and fine-tuning in two sentences."

    if provider not in PROVIDERS:
        raise ValueError(f"Unknown provider '{provider}'. Choose from {list(PROVIDERS)}")

    print(f"Provider: {provider}\n")
    print(PROVIDERS[provider](prompt))


if __name__ == "__main__":
    main()
