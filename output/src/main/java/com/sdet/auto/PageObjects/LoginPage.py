
from playwright.sync_api import Page

def enter_credentials(page: Page, user_id: str, password: str):
    page.fill(txtUsername, user_id)
    page.fill(txtPassword, password)
    page.click(btnLogin)

def verify_message(page: Page, expected_msg: str):
    actual_msg = page.get_by_selector(lblMessage).text_content()
    assert expected_msg in actual_msg