# Implementation Plan

This document outlines the development phases for the SecondSelf project, breaking down the work into logical, sequential steps.

## Phase 0: Project Setup

*   **Goal:** Initialize the project structure.
*   **Tasks:**
    *   Create the main directory structure (`raw/`, `wiki/`, `storage/`).
    *   Create subdirectories for PARA method (`wiki/Projects`, `wiki/Areas`, etc.).
    *   Initialize placeholder files (`app.py`, `graph.json`, `requirements.txt`).
    *   Set up the `.gitignore` file.

## Phase 1: The Archivist (Capture)

*   **Goal:** Implement the single-entry capture pipeline.
*   **Deliverable:** A script `capture.py`.
*   **Tasks:**
    *   Use `argparse` to handle command-line inputs for `type` (`note`, `link`, `file`) and `content`.
    *   Generate a UUID and timestamp for each capture.
    *   For `file` type, copy the source file to the `storage/` directory.
    *   Create a JSON object with the capture metadata.
    *   Save the JSON object to the `raw/` directory.

## Phase 2: The Librarian (AI Processing)

*   **Goal:** Automate the organization and linking of knowledge.
*   **Deliverable:** A script `process.py`.
*   **Sub-Phase 2.1: Ingestion & Content Extraction**
    *   Scan the `raw/` directory for new JSON files.
    *   For `link` types, use `requests` and `BeautifulSoup4` to scrape web page content.
    *   For `file` types (e.g., `.txt`), read the content from the `storage/` directory.
*   **Sub-Phase 2.2: AI Classification & Metadata Generation**
    *   Integrate with a Generative AI API (e.g., Gemini).
    *   Create a prompt that instructs the AI to generate a `title`, `summary`, `para_category`, and `tags` from the extracted content.
    *   Parse the AI's response.
*   **Sub-Phase 2.3: Embedding & Auto-Linking**
    *   Generate an embedding vector for the note's content using an embedding model.
    *   Store the embedding (e.g., in a `.pkl` file or directly in the Markdown frontmatter).
    *   For each new note, compare its embedding to all existing notes to find related items.
*   **Sub-Phase 2.4: Storage**
    *   Create a Markdown file with all metadata in YAML frontmatter.
    *   Save the file to the correct PARA subdirectory within `wiki/`.
    *   Archive the processed JSON file from `raw/`.

## Phase 3: The Cartographer (Graph Generation)

*   **Goal:** Create a visualizable representation of the knowledge graph.
*   **Deliverable:** An updated `graph.json`.
*   **Tasks:**
    *   Create a script `build_graph.py`.
    *   Parse all Markdown files in the `wiki/` directory.
    *   Extract metadata (`id`, `title`, `category`, `related_notes`) from each file.
    *   Build the `nodes` and `links` lists.
    *   Overwrite `graph.json` with the new data.

## Phase 4: The Oracle (Q&A and Deployment)

*   **Goal:** Build the user interface and deploy the application.
*   **Deliverable:** A deployed Streamlit application.
*   **Tasks:**
    *   Develop the Streamlit UI in `app.py`.
    *   Implement a graph visualization component that reads `graph.json`.
    *   Build the RAG (Retrieval-Augmented Generation) pipeline for answering questions.
    *   Deploy the application to a public cloud service (e.g., Streamlit Community Cloud).