# Problem Statement

Every notes app fails the same way: you capture hundreds of notes, bookmarks, PDFs, and ideas — and then you never find them again. Information goes in, but nothing comes back out. Notes sit in folders nobody re-reads. Bookmarks pile up unread. Knowledge doesn’t compound.

**Goal:** Build an end-to-end system where you can capture anything (a note, a link, a file), have AI automatically classify and file it, auto-link it to related knowledge, render it as a live interactive graph you can explore, and — most importantly — ask it any question in plain English and get an answer synthesized from your own accumulated knowledge. Then deploy it to a public URL anyone can open.

Not a notes app. Not a chatbot. A brain that organizes itself and answers for you.

---

## Final System (4-Week Build)

1. Capture any note/link/file  
2. AI classifies & files it (PARA method)  
3. AI auto-links it to related notes (embeddings)  
4. Everything renders as a live, interactive, hoverable graph  
5. Ask it anything in plain English → answer pulled from YOUR notes  
6. Deployed on a public URL anyone can open  

---

## Week-by-Week Problem Statements

### Week 1 — The Archivist: *"Capture Everything, Lose Nothing"*
**Problem:** Ideas, links, and notes scatter across apps, browser tabs, and memory.  
**Goal:** Build the foundation — one command that captures anything into one place.  
**Deliverable:** Capture pipeline that saves notes, links, and files into `raw/` with timestamp + unique ID.  
**Badge:** The Archivist  

---

### Week 2 — The Librarian: *"Teach AI to Organize For You"*
**Problem:** A pile of raw captures is still a mess. Manual tagging never happens.  
**Goal:** Make the AI do the filing and auto-link related notes.  
**Deliverable:** Self-organizing wiki with PARA categorization, tags, summaries, and auto-linked notes.  
**Badge:** The Librarian  

---

### Week 3 — The Cartographer: *"Visualize the Brain"*
**Problem:** Organized notes are invisible without visualization.  
**Goal:** Convert the wiki into a force-directed interactive graph you can explore.  
**Deliverable:** Interactive graph (`graph.json` + JS visualization) showing nodes and links.  
**Badge:** The Cartographer  

---

### Week 4 — The Oracle: *"Ask It Anything, Ship It Public"*
**Problem:** A visual brain is beautiful, but the real payoff is answers.  
**Goal:** Wire up natural-language search over everything you know and deploy it.  
**Deliverable:** Streamlit app with graph + search bar, deployed to a public URL.  
**Badge:** The Oracle  

---

## End-to-End Flow

**Capture → Classify → Link → Graph → Ask → Deploy**

By the end of Week 4, you will have a fully functioning **SecondSelf**:  
- A personal AI brain that organizes itself  
- An interactive graph of your knowledge  
- A retrieval-augmented Q&A system  
- A public deployment anyone can access
