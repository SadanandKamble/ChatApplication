from sentence_transformers import SentenceTransformer # pyright: ignore[reportMissingImports]
import faiss # pyright: ignore[reportMissingImports]
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory FAISS index per user
user_indexes = {}
user_docs = {}

def add_documents(user_id: int, docs: list):
    embeddings = model.encode([doc['content'] for doc in docs])
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    user_indexes[user_id] = index
    user_docs[user_id] = docs

def chat(user_id: int, query: str):
    if user_id not in user_indexes:
        return "No documents found. Please add documents first."
    embedding = model.encode([query])
    D, I = user_indexes[user_id].search(np.array(embedding), k=1)
    matched_doc = user_docs[user_id][I[0][0]]
    return f"Based on your document '{matched_doc['title']}': {matched_doc['content'][:200]}"
