
from playwright.sync_api import Page

class EmailSentPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_email_sent(self, test_assert, expected_msg):
        txt_message = self.page.locator("#content")
        test_assert.set_pass(txt_message.text_content() == expected_msg)