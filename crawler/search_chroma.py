import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="ccr_documents"
)

query = input("Ask a question: ")

results = collection.query(
    query_texts=[query],
    n_results=5
)

for i, doc in enumerate(results["documents"][0]):

    print("\n" + "=" * 60)
    print("Result", i + 1)

    print(
        "Title:",
        results["metadatas"][0][i]["title"]
    )

    print(
        "URL:",
        results["metadatas"][0][i]["url"]
    )

    print("\nContent:")
    print(doc[:500])