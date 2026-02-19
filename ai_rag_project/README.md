AI PDF Question Answering using Endee Vector Store

Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system for question answering over PDF documents. The system extracts text from uploaded PDFs, converts the text into vector embeddings, performs semantic similarity search using a vector store abstraction built around Endee, and generates context-aware answers using a transformer-based question answering model.
The architecture is modular and designed in a way that allows seamless integration with the native Endee vector database engine in production environments.

## System Architecture

User → Streamlit Interface  
→ PDF Text Extraction  
→ Text Chunking  
→ Embedding Generation (SentenceTransformers)  
→ Endee Vector Store Abstraction  
→ Semantic Similarity Search  
→ Question Answering Model (DistilBERT SQuAD)  
→ Final Answer  

## Technologies Used

- Python  
- Streamlit  
- SentenceTransformers  
- HuggingFace Transformers  
- Endee (Vector Database Abstraction Layer)  

## Project Structure

ai_rag_project/
│
├── app.py
├── requirements.txt
├── README.md
├── utils/
│   ├── __init__.py
│   ├── embedding.py
│   ├── vector_store.py
│   └── rag.py

- app.py – Streamlit user interface and application flow  
- embedding.py – Embedding generation logic  
- vector_store.py – Endee vector store abstraction layer  
- rag.py – Question answering logic  

## Key Features

- Upload and process PDF documents  
- Semantic search using vector similarity  
- Context-based question answering  
- Modular and production-style architecture  
- Clean separation of UI, embedding, vector storage, and RAG components  

## Endee Integration

The system uses an EndeeVectorStore abstraction layer to handle vector storage and similarity search. This design allows the in-memory implementation to be replaced with the native Endee engine without modifying the core application logic. The modular approach ensures flexibility, scalability, and production readiness.

## Explanation of the Approach

1. Documents are converted into embeddings using a sentence transformer model.  
2. These embeddings are stored and searched using a vector store abstraction aligned with Endee’s architecture.  
3. When a user asks a question, the most semantically relevant text chunks are retrieved.  
4. A transformer-based QA model generates an answer using only the retrieved context.  

This ensures that answers are grounded in document content rather than generated purely from model memory.

