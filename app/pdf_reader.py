from pypdf import PdfReader
from chunker import chunk_text


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


if __name__ == "__main__":
    pdf_path = "documents/1. Introduction to Machine Learning.pdf"

    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk)