import streamlit as st
import os 

from dotenv import load_dotenv   
load_dotenv()  

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.title("🤞Tasnim Chatbot")
st.write("😎Welcome to the Tasnim Chatbot!")

# session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# show history
for message in st.session_state.conversation:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("✌Type your prompt here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.conversation.append({"role": "user", "content": prompt})

    groq_sys_prompt = ChatPromptTemplate.from_template(
        """You are a helpful assistant.
        Answer directly: {user_prompt}"""
    )

    model = "llama-3.1-8b-instant"

    groq_chat = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name=model
    )

    chain = groq_sys_prompt | groq_chat | StrOutputParser()

    response = chain.invoke({"user_prompt": prompt})

    st.chat_message("assistant").markdown(response)
    st.session_state.conversation.append({"role": "assistant", "content": response})