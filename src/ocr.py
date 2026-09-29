from pathlib import Path
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

RAW = Path("data/raw")
OUT = Path("data/text")
OUT.mkdir(parents=True, exist_ok=True)

for f in sorted(RAW.iterdir()):
    if f.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue
    img = cv2.imread(str(f))
    if img is None:
        print("Could not read", f.name)
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    (OUT / (f.stem + ".txt")).write_text(text, encoding="utf-8")
    print(f.name, "->", len(text), "characters")