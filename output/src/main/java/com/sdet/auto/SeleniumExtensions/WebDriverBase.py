
from playwright.sync_api import Page, Browser, BrowserType

def get_web_driver(browser: str) -> Page:
    if browser == "chrome":
        browser = BrowserType.launch(executable_path="path/to/chrome", headless=False)
        page = browser.new_page()
        page.set_viewport_size(width=1920, height=1080)
        page.set_default_navigation_timeout(timeout=0)
        return page
    elif browser == "firefox":
        browser = BrowserType.launch(executable_path="path/to/firefox", headless=False)
        page = browser.new_page()
        page.set_viewport_size(width=1920, height=1080)
        page.set_default_navigation_timeout(timeout=0)
        return page
    elif browser == "seleniumGrid":
        browser = BrowserType.connect(ws_endpoint="ws://SESYNPZ6.gridlastic.com:80/wd/hub", headless=False)
        page = browser.new_page()
        page.set_viewport_size(width=1920, height=1080)
        page.set_default_navigation_timeout(timeout=0)
        return page
    else:
        raise Exception(f"Browser type {browser} is not supported.")