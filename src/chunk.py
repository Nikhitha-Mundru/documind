import json
from pathlib import Path

TEXT_DIR = Path("data/text")
OUT = Path("data/chunks/chunks.json")
OUT.parent.mkdir(parents=True, exist_ok=True)


def split_text(text, size=800, overlap=100):
    text = " ".join(text.split())
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        if start + size >= len(text):
            break
        start += size - overlap
    return chunks


records = []
for f in sorted(TEXT_DIR.glob("*.txt")):
    for i, chunk in enumerate(split_text(f.read_text(encoding="utf-8"))):
        if len(chunk.strip()) < 30:
            continue
        records.append({"id": f"{f.stem}_c{i}", "source": f.stem, "text": chunk})

OUT.write_text(json.dumps(records, indent=2), encoding="utf-8")
print("Wrote", len(records), "chunks")