import os
import json

def build_graph():
    captures_path = "captures.json"
    nodes = []
    links = []

    if os.path.exists(captures_path):
        with open(captures_path, "r", encoding="utf-8") as f:
            captures = json.load(f)

        for idx, item in enumerate(captures, start=1):
            node_id = str(idx)
            nodes.append({"id": node_id, "label": item.get("title", f"Note {idx}")})
            if idx > 1:
                links.append({"source": str(idx - 1), "target": node_id})
    else:
        nodes.append({"id": "1", "label": "Start"})
        links.append({"source": "1", "target": "1"})

    graph = {"nodes": nodes, "links": links}
    with open("graph.json", "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)

    print(f"Graph build complete. Found {len(nodes)} nodes and {len(links)} links.")
    print("Graph data saved to 'graph.json'")

if __name__ == "__main__":
    build_graph()
