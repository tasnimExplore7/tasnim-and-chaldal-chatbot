import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


# LangChain 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from langchain_groq import ChatGroq


st.title("🎁Chaldal Chatbot")
st.write("😊Ask anything about vegetable prices from Chaldal")

# Store chat history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display chat history
for message in st.session_state.conversation:
    st.chat_message(message["role"]).markdown(message["content"])


# Vectorstore Creation
@st.cache_resource
def get_vectorstore():
    pdf_file = "./vegetables.pdf"

    # Load PDF
    loader = PyPDFLoader(pdf_file)
    documents = loader.load()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Create vector database
    vectorstore = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="./chroma_db"  # optional persistence
    )

    return vectorstore


# LLM Setup (Groq)
def get_llm():
    return ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )


# Chat Input
prompt = st.chat_input("Ask something about the vegetables...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.conversation.append(
        {"role": "user", "content": prompt}
    )

    try:
        # Load vectorstore
        vectorstore = get_vectorstore()
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # Retrieve relevant docs
        docs = retriever.invoke(prompt)

        if not docs:
            response = "I couldn't find relevant information in the document."
        else:
            # Combine context
            context = "\n\n".join([doc.page_content for doc in docs])

            # Build prompt
            final_prompt = f"""
You are a helpful assistant.

Answer the question based ONLY on the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{prompt}
"""

            # Get LLM response
            llm = get_llm()
            response = llm.invoke(final_prompt).content

        # Show assistant response
        st.chat_message("assistant").markdown(response)
        st.session_state.conversation.append(
            {"role": "assistant", "content": response}
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")