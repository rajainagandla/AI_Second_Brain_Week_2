# Edge Cases and Corner Scenarios

This document lists potential edge cases and failure modes for the SecondSelf project to consider during development and testing.

## Phase 1: Capture (The Archivist)

*   **Invalid Input:** The `capture.py` script is called with an invalid `type` (e.g., `capture.py image ...`). The script should fail gracefully with a clear error message.
*   **Missing Content:** The script is called without any content (e.g., `capture.py note`).
*   **File Not Found:** The script is called with `type="file"` but the provided path is invalid.
*   **Permissions Error:** The script cannot write to the `raw/` or `storage/` directories due to file system permissions.
*   **Very Large Files:** Capturing an extremely large file could lead to long copy times or excessive disk usage.

## Phase 2: Processing (The Librarian)

*   **Network Failure:** A `link` cannot be scraped because of a network error or a 404 Not Found status.
*   **Scraping Protection:** A target website has anti-scraping measures (e.g., Cloudflare, JavaScript rendering), resulting in empty or garbage content.
*   **Unsupported File Types:** The system is asked to process a file it cannot parse (e.g., a video file, a proprietary document format).
*   **API Failures:** The Generative AI API is down, returns an error, or exceeds rate limits. The processing script should handle this by retrying or skipping the item.
*   **Malformed AI Response:** The AI returns a response that is not valid JSON or does not contain the expected fields (`title`, `summary`, etc.).
*   **Empty/Low-Quality Content:** The content sent to the AI is too short or nonsensical, leading to poor quality summaries and tags.
*   **No Existing Notes:** The auto-linking mechanism runs for the very first time when there are no other notes to compare against.

## Phase 3: Graphing (The Cartographer)

*   **Empty Wiki:** The `build_graph.py` script runs when the `wiki/` directory is empty. It should produce an empty `graph.json` without errors.
*   **Malformed Frontmatter:** A Markdown file has corrupted or missing YAML frontmatter, causing parsing errors.
*   **Performance:** The knowledge base grows to thousands of nodes, making graph generation and frontend rendering very slow.

## Phase 4: Q&A (The Oracle)

*   **No Relevant Context:** A user asks a question for which there are no relevant notes in the knowledge base. The system should respond gracefully (e.g., "I couldn't find an answer in your notes.").
*   **Ambiguous Questions:** The user's query is too vague to yield useful search results.
*   **Out-of-Context Questions:** The user asks a general knowledge question. The model should be instructed to only use the provided context from the user's notes.
*   **Streaming Errors:** The connection to the Streamlit frontend is lost while an answer is being streamed.