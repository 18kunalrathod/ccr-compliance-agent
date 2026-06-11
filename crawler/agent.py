import os
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Connect to Chroma
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("ccr_documents")

while True:
    question = input("\nAsk a question (or 'quit'): ")

    if question.lower() == "quit":
        break

    # Search Chroma
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    contexts = []
    citations = []

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):
        contexts.append(doc)
        citations.append(meta["url"])

    context_text = "\n\n".join(contexts)

    # Limiting my token usage 
    context_text = context_text[:4000]

    prompt = f"""
You are a DIR compliance assistant.

Answer using only the provided context.

Context:
{context_text}

Question:
{question}

Answer:
"""

    print("\nSending request to Gemini...")
    print("Context length:", len(context_text))

    try:
        response = model.generate_content(prompt)

        print("\nAnswer:")
        print(response.text)

        print("\nSources:")
        for url in set(citations):
            print("-", url)

    except Exception as e:
        print("\nGemini API Error:")
        print(e)
        print("\nCheck your API key, quota, or billing settings.")
        continue