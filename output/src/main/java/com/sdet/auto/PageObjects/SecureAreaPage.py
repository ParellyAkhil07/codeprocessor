
from playwright.sync_api import Page

class SecureAreaPage:
    def __init__(self, page: Page):
        self.page = page
        self.lblMessage = page.locator("#flash")
        self.btnLogout = page.locator(".icon-2x.icon-signout")

    def verifyMessage(self, expectedMsg: str):
        assert expectedMsg in self.lblMessage.text_content()

    def clickLogoutButton(self):
        self.btnLogout.click()