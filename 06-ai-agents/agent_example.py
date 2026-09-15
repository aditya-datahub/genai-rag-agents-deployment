"""
Minimal tool-using AI agent built with LangChain.

Gives the LLM two tools — a calculator and a mock "search" tool — and lets it
decide when to call them to answer a question that requires both reasoning
and a lookup.

Usage:
    python agent_example.py
"""

import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression, e.g. '23 * 4 + 1'."""
    try:
        # NOTE: eval is used here only for a controlled, educational demo.
        # In production, use a safe math parser instead of eval.
        allowed_chars = set("0123456789+-*/(). ")
        if not set(expression) <= allowed_chars:
            return "Error: expression contains disallowed characters."
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {e}"


@tool
def mock_search(query: str) -> str:
    """Look up a fact from a small mock knowledge base (stand-in for a real search API)."""
    fake_kb = {
        "population of france": "France has a population of approximately 68 million people.",
        "capital of japan": "The capital of Japan is Tokyo.",
    }
    return fake_kb.get(query.lower().strip(), "No results found in mock search.")


def build_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [calculator, mock_search]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Use tools when they help "
                       "you answer accurately, and show your reasoning briefly."),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=5)


def main():
    executor = build_agent()
    question = (
        "What's the population of France, and what would that number be "
        "if it doubled?"
    )
    result = executor.invoke({"input": question})
    print("\nFinal answer:", result["output"])


if __name__ == "__main__":
    main()
