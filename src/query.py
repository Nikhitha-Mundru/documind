import chromadb

client = chromadb.PersistentClient(path="chroma_db")
col = client.get_collection("docs")

q = input("Question: ")
res = col.query(query_texts=[q], n_results=3)

for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
    print(f"\n[{meta['source']}] distance {dist:.2f}")
    print(doc[:300])