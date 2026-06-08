from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        print("Opening Westlaw...")

        page.goto(
    "https://govt.westlaw.com/calregs",
    wait_until="domcontentloaded",
    timeout=120000
)

        print("Waiting 30 seconds...")

        print("Complete the Cloudflare verification in the browser.")
        input("Press Enter here after you reach the actual website...")

        with open("westlaw_page.html", "w", encoding="utf-8") as f:
            f.write(page.content())

        print("Screenshot saved")
        print("HTML saved")

        browser.close()

if __name__ == "__main__":
    main()