from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings
if __name__ == "__main__":
    test_chunks = [
        "Machine learning is a field of artificial intelligence.",
        "Reinforcement learning learns through rewards."
    ]

    embeddings = create_embeddings(test_chunks)

    print("Number of embeddings:", len(embeddings))
    print("Embedding size:", len(embeddings[0]))