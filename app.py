import os
import json
import google.genai as genai
import chromadb
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize Gemini client
client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-1.5-flash")

# Initialize ChromaDB in embedded mode
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="second_self")

# Streamlit UI
st.set_page_config(page_title="SecondSelf: A Self-Organizing AI Brain", layout="wide")
st.title("SecondSelf: A Self-Organizing AI Brain")

st.subheader("Knowledge Graph")
st.write("Category Legend:")
st.markdown("- 🔴 Projects\n- 🔵 Areas\n- 🟢 Resources\n- ⚪ Archive\n- ⚫ Uncategorized")

if os.path.exists("graph.json"):
    with open("graph.json", "r", encoding="utf-8") as f:
        graph_data = json.load(f)
    nodes = [Node(id=node["id"], label=node["label"], size=20) for node in graph_data.get("nodes", [])]
    edges = [Edge(source=edge["source"], target=edge["target"]) for edge in graph_data.get("links", [])]

    config = Config(width=800, height=600, directed=True, physics=True)
    agraph(nodes=nodes, edges=edges, config=config)
else:
    st.warning("Your knowledge graph is empty. Run process.py and build_graph.py to populate it.")

st.subheader("Ask Your Brain")
query = st.text_input("Ask a question based on your knowledge base:")

if query:
    try:
        response = chat.send_message(query)
        st.write("Answer:", response.text)
    except Exception as e:
        st.error(f"Error querying Gemini: {e}")
