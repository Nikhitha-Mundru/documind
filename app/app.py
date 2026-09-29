import time
import chromadb
import streamlit as st
from google import genai

st.set_page_config(page_title="DocuMind", page_icon="📄")
st.title("📄 DocuMind")
st.caption("Ask questions about scanned documents. Answers cite their source files.")


@st.cache_resource
def load():
    col = chromadb.PersistentClient(path="chroma_db").get_collection("docs")
    return col, genai.Client()


col, llm = load()

q = st.text_input("Your question")

if q:
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

    st.subheader("Answer")
    st.write(r.text)
    st.caption(f"Response time: {time.time() - start:.1f}s")

    st.subheader("Sources")
    for s, c in zip(sources, chunks):
        with st.expander(s):
            st.write(c)