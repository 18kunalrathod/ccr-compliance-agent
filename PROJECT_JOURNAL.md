# Development Journal

## CCR/DIR Compliance Agent

This document captures the development process, experiments and challenges while building the CCR/DIR Compliance Agent.

---

# Day 1 — Project Setup & Requirements Analysis

## Goals

* Understand assignment requirements
* Explore potential data sources
* Set up the development environment
* Evaluate possible crawling solutions

## Activities

* Created the project repository and folder structure
* Configured a Python virtual environment
* Installed required dependencies
* Researched California Department of Industrial Relations (DIR) resources
* Evaluated Crawl4AI as the primary crawling framework

## Key Observations

At this stage, the primary objective was understanding how compliance-related content could be collected and transformed into a searchable knowledge base.

The project direction became clear:

```text
Website Content
      ↓
Content Extraction
      ↓
Vector Database
      ↓
LLM-Powered Search
```

## Outcome

Successfully prepared the development environment and established the initial project architecture.

---

# Day 2 — Crawling Research & Website Accessibility

## Goals

* Retrieve compliance-related documents
* Evaluate website accessibility
* Test automated crawling approaches

## Activities

* Built the first Crawl4AI crawler
* Tested automated content extraction
* Investigated browser-based crawling alternatives
* Explored Playwright for browser automation

## Findings

Several target pages were protected by Cloudflare.

Testing produced the following results:

| Method         | Result            |
| -------------- | ----------------- |
| Crawl4AI       | Blocked           |
| Playwright     | Verification Loop |
| Manual Browser | Successful        |

The results indicated that the challenge was not website availability, but automation detection.

## Outcome

Identified anti-bot protection as the primary obstacle to automated content collection.

---

# Day 3 — Browser Automation Experiments

## Goals

* Improve crawler reliability
* Reduce automation fingerprints
* Investigate alternative crawling strategies

## Activities

Implemented and tested multiple browser configurations:

### Experiments Performed

#### Stealth Mode

Attempted to reduce automation signals.

**Result:** Blocked.

#### Persistent Browser Profile

Stored browser state across sessions.

**Result:** Blocked.

#### Delayed Execution

Introduced wait periods before requests.

**Result:** Blocked.

## Key Learning

Modern anti-bot systems evaluate much more than browser fingerprints. Simply emulating a browser is not always sufficient to bypass detection.

## Outcome

Concluded that additional browser configuration alone would not solve the crawling challenge.

---

# Day 4 — Building the Content Processing Pipeline

## Goals

* Create a structured extraction workflow
* Store collected documents locally
* Preserve metadata for future retrieval

## Activities

Implemented:

* URL discovery workflow
* Page extraction workflow
* Metadata storage

Pipeline:

```text
Discover URLs
      ↓
Extract Content
      ↓
Store Documents
```

Generated files:

```text
discovered_urls.json
pages.jsonl
```

Stored information included:

* Source URL
* Page Title
* Extracted Markdown Content

## Outcome

Successfully created a reusable document collection pipeline.

---

# Day 5 — Document Chunking & Vector Database Integration

## Goals

* Prepare documents for semantic retrieval
* Build the vector search layer

## Activities

Implemented:

* Document chunking
* ChromaDB integration
* Retrieval testing

Pipeline:

```text
pages.jsonl
      ↓
Document Chunking
      ↓
chunks.jsonl
      ↓
ChromaDB
```

## Results

* Split large documents into manageable chunks
* Preserved metadata and source information
* Created ChromaDB collection:

```text
DIR_documents
```

* Verified semantic retrieval using test queries

## Key Learning

Chunking plays a critical role in retrieval quality. Smaller, focused chunks significantly improve search relevance.

## Outcome

Completed the retrieval layer of the RAG architecture.

### Note

179 internal URLs were discovered during crawling. After filtering inaccessible, duplicate, or non-content pages, 168 pages were successfully extracted and processed.

---

# Day 6 — Gemini Integration & End-to-End RAG System

## Goals

* Generate grounded answers
* Complete the Retrieval-Augmented Generation workflow
* Add source citations

## Activities

Integrated:

* Gemini 2.5 Flash
* ChromaDB retrieval
* Citation generation
* Error handling

Final architecture:

```text
User Question
      ↓
ChromaDB Retrieval
      ↓
Relevant Document Chunks
      ↓
Gemini 2.5 Flash
      ↓
Answer Generation
      ↓
Source Citations
```

## Optimization

To reduce API usage:

```python
n_results = 3
context_text = context_text[:4000]
```

Benefits:

* Reduced token consumption
* Faster responses
* Lower API costs

## Challenges

### API Quota Limits

Encountered:

```text
429 RESOURCE_EXHAUSTED
```

Resolution:

* Validated API configuration
* Switched to supported Gemini model
* Reduced context size
* Added error handling

## Final Outcome

Successfully built a working Retrieval-Augmented Generation (RAG) system capable of:

* Discovering and processing compliance documents
* Storing vector embeddings
* Performing semantic retrieval
* Generating grounded answers
* Displaying source citations

---

# Key Learnings

### Retrieval-Augmented Generation

Learned how modern AI systems combine:

* Vector retrieval
* Context augmentation
* Large Language Models

to produce grounded responses.

### Vector Databases

Gained practical experience with:

* ChromaDB
* Semantic search
* Embedding-based retrieval

### Crawling Challenges

Learned how Cloudflare and anti-bot systems impact automated content collection.

### Production Considerations

Explored:

* API quota management
* Token optimization
* Error handling
* Environment variable security



## Project Statistics

| Component           | Result           |
| ------------------- | ---------------- |
| URLs Discovered     | 179              |
| Pages Extracted     | 179              |
| ChromaDB Collection | dir_documents    |
| Document Chunks     | 3376             |
| Vector Database     | ChromaDB         |
| LLM                 | Gemini 2.5 Flash |
| Retrieval Method    | Semantic Search  |
| Citations           | Supported        |
