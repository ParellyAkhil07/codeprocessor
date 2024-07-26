
from playwright.sync_api import Page

class EmailSentPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_email_sent(self, expected_msg: str) -> bool:
        actual_msg = self.page.locator("#content").text_content()
        return expected_msg == actual_msg