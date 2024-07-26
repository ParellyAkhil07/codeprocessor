
from playwright.sync_api import Page

def verify_message(page: Page, expected_msg: str) -> bool:
    actual_msg = page.locator("#flash").text_content()
    return expected_msg in actual_msg

def click_logout_button(page: Page) -> None:
    page.locator(".icon-2x.icon-signout").click()