"""
Minimal GenAI chatbot with a Streamlit UI and LangChain-backed conversation
memory.

Run with:
    streamlit run chatbot_streamlit.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="GenAI Chatbot", page_icon="💬")
st.title("💬 GenAI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a concise, friendly assistant.")
    ]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Render existing conversation
for msg in st.session_state.messages[1:]:  # skip system message
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# Handle new input
if user_input := st.chat_input("Type a message..."):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = llm.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)
