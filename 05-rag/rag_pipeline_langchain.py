"""
Minimal Retrieval-Augmented Generation (RAG) pipeline.

Loads a text file, chunks it, embeds the chunks into a Chroma vector store,
retrieves the most relevant chunks for a query, and asks an LLM to answer
using only that retrieved context.

Usage:
    python rag_pipeline.py
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

SAMPLE_DOC_PATH = "sample_docs/knowledge_base.txt"


def build_sample_doc_if_missing():
    """Create a tiny sample knowledge base so the script runs out of the box."""
    os.makedirs("sample_docs", exist_ok=True)
    if not os.path.exists(SAMPLE_DOC_PATH):
        with open(SAMPLE_DOC_PATH, "w") as f:
            f.write(
                "Retrieval-Augmented Generation (RAG) combines a retriever and a "
                "generator. The retriever fetches relevant chunks of text from a "
                "knowledge base using vector similarity search. The generator "
                "(an LLM) then uses those chunks as context to produce a grounded, "
                "up-to-date answer instead of relying solely on its training data.\n\n"
                "Vector stores such as Chroma, FAISS, and Pinecone index document "
                "embeddings so that semantically similar text can be retrieved "
                "quickly at query time.\n\n"
                "Chunking strategy matters: chunks that are too large dilute "
                "relevance, while chunks that are too small lose context. A common "
                "starting point is 500 tokens with 50 tokens of overlap."
            )


def load_and_split(path: str):
    loader = TextLoader(path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)


def build_vectorstore(chunks):
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")


def build_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template(
        "Answer the question using ONLY the context below. "
        "If the answer isn't in the context, say you don't know.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


def main():
    build_sample_doc_if_missing()
    chunks = load_and_split(SAMPLE_DOC_PATH)
    vectorstore = build_vectorstore(chunks)
    chain = build_rag_chain(vectorstore)

    question = "What is RAG and why does chunking strategy matter?"
    answer = chain.invoke(question)

    print(f"Q: {question}\n")
    print(f"A: {answer}")


if __name__ == "__main__":
    main()
