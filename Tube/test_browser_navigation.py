from playwright.sync_api import Page


def test_has_title(page: Page):
    page.goto('https://www.instagram.com/')

# Use XPath syntax by prefixing the selector with 'xpath=' so Playwright does not parse it as CSS.
    page.locator('xpath=/html/body/div[1]/div/div/div[2]/div/div/div[1]'
                 '/div[1]/div/div/div/div[1]/div/div[3]/div/div/div[2]/button/span').click()

    # Go back using browser navigation buttons.
    page.go_back()

    # Go forward using browser navigation buttons.
    page.go_forward()

    # Reload page using browser reload button.
    page.reload()

    page.wait_for_timeout(5000)
