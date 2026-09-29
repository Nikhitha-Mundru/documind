import json
import chromadb

client = chromadb.PersistentClient(path="chroma_db")
col = client.get_or_create_collection("docs")

with open("data/chunks/chunks.json", encoding="utf-8") as f:
    records = json.load(f)

col.upsert(
    ids=[r["id"] for r in records],
    documents=[r["text"] for r in records],
    metadatas=[{"source": r["source"]} for r in records],
)
print("Indexed", col.count(), "chunks")