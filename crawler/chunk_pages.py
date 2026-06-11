import json

CHUNK_SIZE = 1000

with open("data/pages.jsonl", "r", encoding="utf-8") as infile, \
     open("data/chunks.jsonl", "w", encoding="utf-8") as outfile:

    for line in infile:
        page = json.loads(line)

        content = page["content_markdown"]

        chunks = [
            content[i:i + CHUNK_SIZE]
            for i in range(0, len(content), CHUNK_SIZE)
        ]

        for idx, chunk in enumerate(chunks):

            chunk_data = {
                "chunk_id": f"{page['url']}#{idx}",
                "url": page["url"],
                "title": page["title"],
                "text": chunk
            }

            outfile.write(
                json.dumps(chunk_data, ensure_ascii=False)
                + "\n"
            )

print("Chunking complete!")