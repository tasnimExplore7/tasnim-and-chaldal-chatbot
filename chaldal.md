#  Chaldal Vegetable Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, ChromaDB, HuggingFace Embeddings, and Groq LLM.
The chatbot answers user questions about vegetable prices and information extracted from Chaldal's vegetable category data.

---

# 📌 Project Overview

The Chaldal Vegetable Chatbot is a conversational AI application that allows users to ask questions related to vegetables and pricing information extracted from Chaldal's vegetable product listings.

The project demonstrates how Retrieval-Augmented Generation (RAG) systems work by combining:

* PDF document processing
* Semantic search
* Vector databases
* Embedding models
* Large Language Models (LLMs)

This project reflects practical skills in AI application development, document retrieval systems, and conversational interfaces.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Extract and utilize vegetable-related information
* Build a RAG-based chatbot system
* Enable intelligent question-answering from documents
* Implement semantic search using vector embeddings
* Create an interactive AI chatbot interface

---

#  Features

* Interactive Streamlit chatbot UI
* PDF-based knowledge retrieval
* Semantic search using embeddings
* Context-aware AI responses
* Vector database storage with ChromaDB
* Real-time LLM response generation
* Conversation history support
* Fast inference using Groq API

---

#  Technologies Used

* Python
* Streamlit
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq API
* Sentence Transformers
* PyPDF
* dotenv

---

# 📂 Project Structure


chaldal-chatbot/

── chaldal.py 
── chroma_db
── vegetables.pdf
── requirements.txt
── .env
── README.md


## 2. Create Virtual Environment


- python -m venv venv

- Activate the virtual environment:

### Windows


- venv\Scripts\activate


### Mac/Linux

- source venv/bin/activate


## 3. Install Dependencies


- pip install -r requirements.txt


#  Requirements


- streamlit
- python-dotenv

- langchain
- langchain-core
- langchain-community
- langchain-text-splitters
- langchain-huggingface
- langchain-groq

- sentence-transformers
- pypdf

- chromadb
- tiktoken


## 4. Configure Environment Variables

- Create a `.env` file:


- GROQ_API_KEY=your_api_key_here


# ▶️ Run the Application

streamlit run app.py


# 🧠 AI & Embedding Models Used

## LLM

* `llama-3.1-8b-instant`

## Embedding Model

* `all-MiniLM-L6-v2`

---

# 🔄 Application Workflow


Vegetable PDF Data
        ↓
PyPDFLoader
        ↓
Text Chunking
        ↓
HuggingFace Embeddings
        ↓
Chroma Vector Database
        ↓
Retriever Search
        ↓
Groq LLM
        ↓
AI Response


# 📚 Core Functionalities

## 1. PDF Document Loading

The chatbot loads vegetable-related data from a PDF document using `PyPDFLoader`.

---

## 2. Text Chunking

Large text content is split into smaller chunks using `RecursiveCharacterTextSplitter` for efficient retrieval.

---

## 3. Embedding Generation

Text chunks are converted into vector embeddings using HuggingFace sentence transformer models.

---

## 4. Vector Database Storage

Embeddings are stored in ChromaDB for semantic similarity search.

-------

## 5. Context Retrieval

Relevant document chunks are retrieved based on user questions.

---

## 6. AI Response Generation

The retrieved context is passed to the Groq LLM to generate accurate responses.

---

# 💻 Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* AI Chatbot Development
* Vector Databases
* Semantic Search
* LLM Integration
* Prompt Engineering
* Streamlit Development
* Document Processing
* Embedding Models
* LangChain Framework

---

# 🔮 Future Improvements

Possible future enhancements:

* Add multi-document support
* Implement memory-based conversations
* Add multilingual support
* Connect with live Chaldal API
* Add product recommendation system
* Deploy on cloud platforms
* Add voice chatbot functionality
* Improve UI/UX design

---

# 🎓 Learning Outcomes

Through this project, I learned:

* How RAG systems work
* Building AI-powered retrieval applications
* Using vector databases for semantic search
* Integrating LLMs with external knowledge sources
* Developing interactive chatbot interfaces with Streamlit

---

# 🤝 Connect With Me

## 👤 NisHat Tasnim

* LinkedIn: https://www.linkedin.com/in/nishat-tasnim-5b9943251
* 
---

# ⭐ Conclusion

The Chaldal Vegetable Chatbot demonstrates a practical implementation of Retrieval-Augmented Generation (RAG) using modern AI technologies. The project combines document retrieval, semantic search, vector databases, and Large Language Models to create an intelligent conversational assistant capable of answering vegetable-related queries from extracted Chaldal data.
