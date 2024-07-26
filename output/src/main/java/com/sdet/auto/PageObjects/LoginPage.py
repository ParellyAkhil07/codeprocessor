
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    txtUsername = "#username"
    txtPassword = "
    btnLogin = ".fa.fa-2x.fa-sign-in"
    lblMessage = "#flash"

    def enter_credentials(self, user_id, password):
        self.page.fill(self.txtUsername, user_id)
        self.page.fill(self.txtPassword, password)
        self.page.click(self.btnLogin)

    def verify_message(self, test_assert, expected_msg):
        actual_msg = self.page.inner_text(self.lblMessage)
        test_assert.set_pass(expected_msg in actual_msg)