from rag.embedding import EmbeddingModel
from rag.vector_store import FAISSStore

class VectorRetriever:
    def __init__(self, docs):
        self.embedder = EmbeddingModel()
        embeddings = self.embedder.encode(docs)

        self.store = FAISSStore(len(embeddings[0]))
        self.store.add(embeddings, docs)

    def query(self, query):
        q_emb = self.embedder.encode([query])[0]
        results = self.store.search(q_emb)
        return "\n".join(results)