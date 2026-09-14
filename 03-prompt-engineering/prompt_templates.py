"""
Compares zero-shot vs. few-shot prompting for a sentiment classification task,
using LangChain prompt templates.

Usage:
    python prompt_templates.py
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def zero_shot_classify(review: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Classify the sentiment of this review as Positive, Negative, or "
        "Neutral. Respond with only the label.\n\nReview: {review}"
    )
    chain = prompt | llm
    return chain.invoke({"review": review}).content


def few_shot_classify(review: str) -> str:
    examples = [
        {"review": "This product exceeded my expectations!", "label": "Positive"},
        {"review": "Terrible quality, broke after one use.", "label": "Negative"},
        {"review": "It's okay, does what it says.", "label": "Neutral"},
    ]

    example_prompt = ChatPromptTemplate.from_messages(
        [("human", "{review}"), ("ai", "{label}")]
    )

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Classify review sentiment as Positive, Negative, or Neutral. "
                       "Respond with only the label."),
            few_shot_prompt,
            ("human", "{review}"),
        ]
    )

    chain = final_prompt | llm
    return chain.invoke({"review": review}).content


def main():
    review = "Shipping was slow but the product itself works great."

    print("Zero-shot result:", zero_shot_classify(review))
    print("Few-shot result:", few_shot_classify(review))


if __name__ == "__main__":
    main()
