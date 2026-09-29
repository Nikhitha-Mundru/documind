# DocuMind: RAG Assistant for Scanned Documents
RAG Assistant that answers questions over scanned documents using OCR, embeddings and cited sources.
Ask natural-language questions about scanned and photographed documents and get answers with cited source files.

## Pipeline
1. OCR: Tesseract + OpenCV (grayscale, upscaling)
2. Chunking: 800-character overlapping chunks, each keeping its source file
3. Embeddings and search: Chroma vector database
4. Answering: Gemini, using only the retrieved chunks, with source citations
5. Demo: Streamlit app

## Results
- Documents indexed: X
- Retrieval hit rate @3: 90% (27/30 test questions)
- Average response time: X s (5 queries)

## Known limitations
- OCR struggles with stylized fonts (for example poster titles), so text in those regions can be lost.
- Evaluation covers 30 questions from a subset of the documents.

## Run it
pip install -r requirements.txt
python src/ocr.py
python src/chunk.py
python src/index.py
python -m streamlit run app/app.py

Set GEMINI_API_KEY in your environment first.
