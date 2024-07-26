
from playwright.sync_api import Page

def get_element_by_selector(page: Page, css_selector: str) -> Page:
    return page.wait_for_selector(css_selector)

def screenshot(page: Page) -> None:
    screenshot = page.screenshot()
    with open("screenshot.png", "wb") as file:
        file.write(screenshot)