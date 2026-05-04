# AI Logistics Assistant

An AI-powered logistics query assistant built using Retrieval-Augmented Generation (RAG), FastAPI, vector search, and LLM-based response generation.

## Overview

This project helps answer logistics-related customer queries such as:

- Delivery policy
- Refund policy
- Shipment delays
- Operational issues

It retrieves relevant logistics policy context and generates accurate responses using an LLM.

---

## Tech Stack

- Python
- FastAPI
- LangChain
- Hugging Face Embeddings
- Vector Store
- Groq LLM API
- MySQL
- HTML/CSS frontend

---

## Architecture

User Query
↓
FastAPI API
↓
Vector Similarity Search
↓
Retrieve Relevant Context
↓
LLM Response Generation
↓
Store Query Logs in MySQL
↓
Frontend Response

---

## Features

- Retrieval-Augmented Generation
- Logistics-specific knowledge retrieval
- Query-response logging
- REST API endpoints
- Interactive frontend
- Context-aware responses

---

## Example Query

**Input**

What is the delivery policy?

**Output**

Standard delivery takes 2-5 days. Delays may occur due to traffic, weather, or operational issues.

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run backend

```bash
python -m uvicorn app.main:app --reload
```

### Open frontend

Open:

frontend/index.html

---

## Future Improvements

- Conversation memory
- Better retrieval ranking
- AWS deployment
- Advanced chunking
