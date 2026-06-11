# DIR Compliance Agent

A Retrieval-Augmented Generation (RAG) assistant built to answer California Department of Industrial Relations (DIR) compliance questions using official DIR website content.

## Overview

This project crawls compliance-related pages from the California DIR website, stores the content in a vector database (ChromaDB), retrieves relevant information based on user queries, and uses Google's Gemini API to generate grounded answers.

The system follows a RAG architecture:

User Question
      ↓
ChromaDB Retrieval
      ↓
Relevant DIR Documents
      ↓
Gemini 2.5 Flash
      ↓
Answer + Source Citations

---

## Features

- Crawl DIR website pages
- Extract and store page content
- Chunk large documents
- Store embeddings in ChromaDB
- Semantic search using vector retrieval
- Gemini-powered answer generation
- Source citation support
- Token usage optimization

---

## Tech Stack

### Backend
- Python
- Crawl4AI
- ChromaDB
- Google Gemini API
- python-dotenv

### Data Storage
- JSON
- ChromaDB Vector Store

---

## Project Structure

```text
ccr-compliance-agent/
│
├── crawler/
│   ├── test_crawl.py
│   ├── extract_pages.py
│   ├── chunk_pages.py
│   ├── load_chroma.py
│   ├── search_chroma.py
│   └── agent.py
│
├── data/
│   ├── discovered_urls.json
│   ├── pages.jsonl
│   └── chunks.jsonl
│
├── chroma_db/
│
├── .env
├── .gitignore
└── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd ccr-compliance-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Pipeline

### Step 1: Crawl DIR Website

```bash
python crawler/test_crawl.py
```

This discovers internal DIR links and stores them in:

```text
data/discovered_urls.json
```

---

### Step 2: Extract Page Content

```bash
python crawler/extract_pages.py
```

Output:

```text
data/pages.jsonl
```

---

### Step 3: Create Chunks

```bash
python crawler/chunk_pages.py
```

Output:

```text
data/chunks.jsonl
```

---

### Step 4: Load into ChromaDB

```bash
python crawler/load_chroma.py
```

Creates collection:

```text
ccr_documents
```

---

### Step 5: Run the Compliance Agent

```bash
python crawler/agent.py
```

Example:

```text
Ask a question:
heat illness prevention requirements

Answer:
...

Sources:
https://www.dir.ca.gov/...
```

---

## Architecture

### Retrieval Phase

1. User submits a question.
2. ChromaDB performs semantic similarity search.
3. Top relevant document chunks are retrieved.

### Generation Phase

1. Retrieved chunks are combined into context.
2. Context is sent to Gemini 2.5 Flash.
3. Gemini generates an answer using only retrieved content.
4. Source URLs are displayed.

---

## Token Optimization

To reduce Gemini API usage:

- Top 3 chunks are retrieved
- Context is limited to 4000 characters
- Only relevant document chunks are sent to Gemini

This helps reduce API costs while maintaining answer quality.

---

## Challenges Faced

### Cloudflare Protection

During early project exploration, several CCR-related sources were protected by Cloudflare and anti-bot mechanisms, which limited automated crawling. To complete the end-to-end RAG pipeline, the final implementation was built using publicly accessible California DIR content.

Approaches explored:

- Crawl4AI
- Playwright browser automation
- Persistent browser profiles

### API Quota Limits

While testing, Gemini free-tier quota limits were encountered.

Mitigations:

- Reduced retrieval size
- Context length limiting
- Error handling for quota exhaustion

---

## Author

Kunal Rathod

Built as a Retrieval-Augmented Generation (RAG) compliance assistant using official California DIR content.