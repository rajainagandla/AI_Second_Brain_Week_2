# System Architecture

This document outlines the architecture for the SecondSelf project, detailing the data models, component design, and deployment strategy.

## 1. Data Models

The system will use distinct data models for raw captured information and for the processed, structured knowledge base.

### 1.1. Raw Capture Object

When any piece of information is first captured, it is stored in a simple, standardized format in the `raw/` directory. Each capture is a single file with a filename convention: `<timestamp>_<uuid>.json`.

**Example (`20260815120000_a1b2c3d4.json`):**
```json
{
  "id": "a1b2c3d4",
  "timestamp": "2026-08-15T12:00:00Z",
  "type": "link", // "note", "link", or "file"
  "content": "https://example.com/article",
  "source_path": null // For 'file' type, the original path of the file
}
```

### 1.2. Processed Knowledge Node

After the AI pipeline processes a raw capture, it is converted into a structured knowledge node. These are stored as individual Markdown files within the self-organizing wiki (e.g., `wiki/Resources/`). Each file contains YAML frontmatter for metadata and the original content.

**Example (`wiki/Resources/a1b2c3d4.md`):**
```markdown
---
id: "a1b2c3d4"
title: "AI-Generated Title of Article"
summary: "This is an AI-generated summary of the content..."
para_category: "Resource"
tags: ["AI", "Knowledge Management", "Productivity"]
embedding_vector: [0.012, -0.045, ..., 0.089]
related_notes: ["e5f6g7h8", "i9j0k1l2"]
source_link: "https://example.com/article"
---

# AI-Generated Title of Article

## Summary
This is an AI-generated summary of the content...

## Full Content / Notes
... (Full text of the note or scraped content from the link) ...
```

### 1.3. Graph Data (`graph.json`)

This file is a machine-readable representation of the entire knowledge graph, generated for the frontend visualization.

```json
{
  "nodes": [
    { "id": "a1b2c3d4", "title": "AI-Generated Title", "category": "Resource" },
    { "id": "e5f6g7h8", "title": "Another Note", "category": "Project" }
  ],
  "links": [
    { "source": "a1b2c3d4", "target": "e5f6g7h8" }
  ]
}
```

## 2. Component Design

The system is broken down into several key components, each corresponding to a major step in the end-to-end flow.

### 2.1. Capture (The Archivist)
*   **Description:** A simple command-line interface (CLI) or script (`capture.py`) that acts as the single entry point for all information.
*   **Functionality:**
    *   Accepts a type (`note`, `link`, `file`) and content.
    *   Generates a unique ID (UUID) and a current timestamp.
    *   Creates a `json` object for the raw capture.
    *   Saves the object to the `raw/` directory. For files, it copies the file to a designated storage area and references its path.

### 2.2. AI Processing Pipeline (The Librarian)
*   **Description:** A core backend script (`process.py`) that orchestrates the AI-driven organization. It can be run on a schedule or triggered when new items appear in `raw/`.
*   **Functionality:**
    1.  **Ingestion:** Scans the `raw/` directory for unprocessed captures.
    2.  **Content Extraction:** For links, it scrapes the content. For files (PDFs, etc.), it extracts the text.
    3.  **AI Classification (LLM Call):** For each capture, it makes an API call to a Large Language Model (e.g., Gemini) to:
        *   Generate a concise `title` and `summary`.
        *   Assign a `para_category` (Project, Area, Resource, Archive).
        *   Extract relevant `tags`.
    4.  **Embedding Generation:** It uses an embedding model to create a vector representation of the note's content.
    5.  **Auto-Linking:** It calculates the cosine similarity between the new note's embedding and all existing notes. Notes with a similarity score above a certain threshold are added to the `related_notes` list.
    6.  **Store:** Creates the final Markdown file with YAML frontmatter and saves it to the appropriate subdirectory within the `wiki/` folder based on its PARA category.

### 2.3. Graph Generation (The Cartographer)
*   **Description:** A script (`build_graph.py`) that transforms the structured wiki into a visualizable format.
*   **Functionality:**
    *   Parses all Markdown files in the `wiki/` directory.
    *   Extracts metadata (`id`, `title`, `category`, `related_notes`) from the YAML frontmatter of each file.
    *   Constructs the `nodes` and `links` arrays.
    *   Writes the final structure to `graph.json`.

### 2.4. Q&A and Visualization (The Oracle)
*   **Description:** A web application built with a framework like Streamlit that serves as the user interface.
*   **Functionality:**
    *   **Graph Visualization:** Uses a JavaScript library (like D3.js or a Python wrapper) to load `graph.json` and render the interactive, force-directed graph.
    *   **Search/Q&A Bar:** Provides a text input for users to ask questions.
    *   **Retrieval-Augmented Generation (RAG):**
        1.  When a question is asked, the app generates an embedding for the query.
        2.  It performs a vector search against the embeddings of all notes in the knowledge base to find the most relevant documents.
        3.  It passes the user's question and the content of the retrieved documents to an LLM.
        4.  The LLM synthesizes an answer based *only* on the provided context from the user's notes.
        5.  The synthesized answer is streamed back to the user in the UI.

## 3. Deployment

*   **Framework:** The final application will be built using **Streamlit**, which simplifies the creation of interactive web apps from Python scripts.
*   **Hosting:** The Streamlit application will be deployed to **Streamlit Community Cloud** (or a similar service like Hugging Face Spaces or Render). This provides a public URL that is easily accessible.
*   **Workflow:** The deployment process will be configured via a GitHub repository. A push to the `main` branch will automatically trigger a redeployment of the application, ensuring the public-facing "brain" is always up-to-date with the latest knowledge.