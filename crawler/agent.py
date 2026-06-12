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


def ask_question(question):

    results = collection.query(
        query_texts=[question],
        n_results=10  #3
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

    try:
        response = model.generate_content(prompt)

        return {
            "answer": response.text,
            "sources": list(set(citations))
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "sources": []
        }


if __name__ == "__main__":

    while True:

        question = input("\nAsk a question (or 'quit'): ")

        if question.lower() == "quit":
            break

        result = ask_question(question)

        print("\nAnswer:")
        print(result["answer"])

        print("\nSources:")
        for url in result["sources"]:
            print("-", url)