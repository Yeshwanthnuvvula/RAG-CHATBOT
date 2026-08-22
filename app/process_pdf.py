from pdf_reader import extract_text_from_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import collection


pdf_path = "documents/1. Introduction to Machine Learning.pdf"


# 1. Extract text from PDF
text = extract_text_from_pdf(pdf_path)


# 2. Split text into chunks
chunks = chunk_text(text)


# 3. Create embeddings
embeddings = create_embeddings(chunks)


# 4. Store chunks and embeddings in ChromaDB
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings.tolist()
)


print("Total chunks:", len(chunks))
print("Total embeddings:", len(embeddings))
print("Stored in ChromaDB:", collection.count())