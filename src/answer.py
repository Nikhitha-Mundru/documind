import time
import chromadb
from google import genai

client_db = chromadb.PersistentClient(path="chroma_db")
col = client_db.get_collection("docs")
llm = genai.Client()

q = input("Question: ")
start = time.time()

res = col.query(query_texts=[q], n_results=3)
chunks = res["documents"][0]
sources = [m["source"] for m in res["metadatas"][0]]

context = "\n\n".join(f"[{s}] {c}" for s, c in zip(sources, chunks))
prompt = (
    "Answer the question using ONLY the context below. "
    "Cite the source in square brackets after each fact, like [file_name]. "
    "If the answer is not in the context, say you cannot find it.\n\n"
    f"Context:\n{context}\n\nQuestion: {q}"
)

r = llm.models.generate_content(model="gemini-3.5-flash", contents=prompt)
print("\nAnswer:", r.text)
print("\nSources:", sorted(set(sources)))
print(f"Time: {time.time() - start:.1f}s")