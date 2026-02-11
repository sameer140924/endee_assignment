from typing import List, Tuple
from utils.embedding import create_embedding

class EndeeVectorStore:
 
    def __init__(self):
        self.stored_chunks: List[str] = []
        self.stored_embeddings: List[List[float]] = []

    def clear_store(self):
        self.stored_chunks.clear()
        self.stored_embeddings.clear()

    def store_text(self, text: str):
        embedding = create_embedding(text)
        self.stored_chunks.append(text)
        self.stored_embeddings.append(embedding)

    def search_similar(self, query: str, top_k: int = 3):
        query_embedding = create_embedding(query)
        scores: List[Tuple[float, str]] = []

        for i, emb in enumerate(self.stored_embeddings):
            score = sum(a * b for a, b in zip(query_embedding, emb))
            scores.append((score, self.stored_chunks[i]))

        scores.sort(reverse=True)
        return [chunk for _, chunk in scores[:top_k]]
