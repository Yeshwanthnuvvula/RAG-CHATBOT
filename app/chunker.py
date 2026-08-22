def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []

    # Clean up excessive whitespace
    words = text.split()

    current_chunk = []

    current_length = 0

    for word in words:
        word_length = len(word) + 1

        if current_length + word_length > chunk_size:
            chunk = " ".join(current_chunk)
            chunks.append(chunk)

            # Keep the last part for overlap
            overlap_words = []
            overlap_length = 0

            for w in reversed(current_chunk):
                if overlap_length + len(w) + 1 > overlap:
                    break

                overlap_words.insert(0, w)
                overlap_length += len(w) + 1

            current_chunk = overlap_words
            current_length = overlap_length

        current_chunk.append(word)
        current_length += word_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks