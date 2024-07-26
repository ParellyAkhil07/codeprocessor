
from playwright.sync_api import Page
from typing import List

def get_element_by_selector(page: Page, css_selector: str) -> List[Page]:
    return page.query_selector_all(css_selector)

def get_element_by_selector(page: Page, css_selector: str, wait_seconds: int) -> List[Page]:
    return page.query_selector_all(css_selector)

def wait_for_element(page: Page, locator: str, wait_seconds: int) -> Page:
    return page.wait_for_selector(locator, timeout=wait_seconds * 1000)

def selenium_exception_handler(page: Page, ex: Exception) -> None:
    exception_name = ex.__class__.__name__
    print(f"WebDriver Exception Handler Caught Exception: [{exception_name}]")
    screenshot(page)
    print("\n")

def screenshot(page: Page) -> None:
    test_name = "test_name"  # Replace with your test name
    screenshot_dir = "/path/to/screenshots"  # Replace with your screenshot directory path

    try:
        print("Attempting Selenium Screenshot ...")
        screenshot = page.screenshot()
        with open(f"{screenshot_dir}/{test_name}.png", "wb") as f:
            f.write(screenshot)
        print(f"Browser Screenshot Save Location: {screenshot_dir}/{test_name}.png")
    except Exception as e:
        print(f"Error taking screenshot: {e}")