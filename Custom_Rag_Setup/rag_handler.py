from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import numpy as np
from ulid import ULID

class VectorStorage:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.PersistentClient(path=".chroma")
        self.collection = self.client.get_or_create_collection(name="aider_rag")
    
    def store_chunks(self, chunks: list[str], metadata: dict = None):
        """Store text chunks with embeddings in ChromaDB"""
        embeddings = self.model.encode(chunks)
        
        # Convert to python lists for Chroma
        embeddings_list = [embedding.tolist() for embedding in embeddings]
        
        # Generate unique IDs
        ids = [str(ULID()) for _ in chunks]
        
        self.collection.add(
            embeddings=embeddings_list,
            documents=chunks,
            ids=ids,
            metadatas=metadata or None
        )
        return ids

    def query_context(self, query: str, n_results: int = 3) -> list[str]:
        """Retrieve relevant context chunks for a query"""
        query_embedding = self.model.encode([query]).tolist()[0]
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results['documents'][0]
