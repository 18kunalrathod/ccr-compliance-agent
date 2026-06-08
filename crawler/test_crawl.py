# import asyncio
# from crawl4ai import AsyncWebCrawler

# async def main():
#     async with AsyncWebCrawler() as crawler:
#         result = await crawler.arun(
#             url="https://govt.westlaw.com/calregs/Document/I7A6B47D0FD4311ECBA0CE8BD2C3F45C2?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)"
#         )

#         print("Success:", result.success)

#         if result.success:
#             print(result.markdown[:1000])
#         else:
#             print(result.error_message)

# asyncio.run(main())


import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig

async def main():

    config = BrowserConfig(
        headless=False,
        enable_stealth=True,
        use_persistent_context=True,
        user_data_dir="./westlaw-profile"
    )

    target_url = "https://govt.westlaw.com/calregs"

    print(f"Starting crawler on {target_url}...")
    print("NOTE: If a browser window opens with a Cloudflare challenge, solve it manually!")

    print("Waiting 15 seconds before starting crawl...")
    await asyncio.sleep(15)

    async with AsyncWebCrawler(config=config) as crawler:

        result = await crawler.arun(
            url=target_url,
            page_timeout=180000
        )

        print("\nSuccess:", result.success)

        if result.success:
            print(result.markdown[:1000])
        else:
            print("Error Message:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())


    # Crawl4ai experiment
    # Blocked by anti-bot protection: Cloudflare JS challenge