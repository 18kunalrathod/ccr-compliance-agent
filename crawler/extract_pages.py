import asyncio
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig

async def main():
    # clear old data set
    with open("data/pages.jsonl", "w", encoding="utf-8") as f:
        pass

    # Load discovered URLs
    with open("data/discovered_urls.json", "r") as f:
        links = json.load(f)

    # # Only test first 5 URLs
    # urls = [link["href"] for link in links[:5]]   #i used this to test crawler


    # crawl all
    urls = [
        link["href"]
        for link in links
        if link["href"].startswith("https://www.dir.ca.gov/")
    ]

    config = BrowserConfig(
        headless=True
    )

    async with AsyncWebCrawler(config=config) as crawler:

        for url in urls:

            print(f"\n{'=' * 60}")
            print(f"Crawling: {url}")

            result = await crawler.arun(url=url)

            if result.success:
                print("SUCCESS")
                print("Title:", result.metadata.get("title", "No Title"))

                page_data = {
                    "url": url,
                    "title": result.metadata.get("title", "No Title"),
                    "content_markdown": result.markdown
                }

                with open("data/pages.jsonl", "a", encoding="utf-8") as outfile:
                    outfile.write(
                        json.dumps(page_data, ensure_ascii=False)
                        + "\n"
                    )

                print("Saved to pages.jsonl")

            else:
                print("FAILED")
                print(result.error_message)

if __name__ == "__main__":
    asyncio.run(main())
