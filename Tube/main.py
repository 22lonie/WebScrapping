import re
from playwright.sync_api import sync_playwright, expect


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://google.com")
        expect(page).to_have_title(re.compile("Google", re.IGNORECASE))
        print(page.title())
        browser.close()


if __name__ == "__main__":
    main()
