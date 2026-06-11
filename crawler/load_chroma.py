import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create local Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="ccr_documents"
)

documents = []
metadatas = []
ids = []

with open("data/chunks.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        chunk = json.loads(line)

        documents.append(chunk["text"])

        metadatas.append({
            "url": chunk["url"],
            "title": chunk["title"]
        })

        ids.append(chunk["chunk_id"])

print("Loaded", len(documents), "chunks")

# Generate embeddings
embeddings = model.encode(
    documents,
    show_progress_bar=True
).tolist()

# Store in Chroma
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print("Successfully loaded into ChromaDB")