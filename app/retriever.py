from app.embeddings import model
from app.vector_store import collection


def search(query, n_results=2):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results


def get_context(query, n_results=2):
    results = search(query, n_results)

    distances = results["distances"][0]

    # If the closest result is too far away,
    # the question is probably unrelated to the documents.
    if distances[0] >= 1.2:
        return ""

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    return context


if __name__ == "__main__":
    query = "What is reinforcement learning?"

    results = search(query)

    for i, document in enumerate(results["documents"][0]):
        print(f"\n--- RESULT {i + 1} ---")
        print(document)