
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def click_forget_password(self):
        self.page.locator("[href='/forgot_password']").click()

    def click_form_authentication(self):
        self.page.locator("[href='/login']").click()

    def verify_on_home_page(self):
        header_text = self.page.locator(".heading").text_content()
        assert header_text == "Welcome to the-internet"