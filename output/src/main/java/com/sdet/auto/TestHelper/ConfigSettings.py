
from playwright.sync_api import Playwright, sync_playwright

def get_web_url():
    return web_url

def set_web_url(url):
    global web_url
    web_url = url

def get_web_browser():
    return web_browser

def set_web_browser(browser):
    global web_browser
    web_browser = browser

def get_config_settings():
    config = {}
    with open("config.properties") as f:
        for line in f:
            key, value = line.split("=")
            config[key] = value.strip()

    set_web_url(config["webUrl"])
    set_web_browser(config["webBrowser"])

    print("Test Config Settings")
    print(f"WebUrl: {get_web_url()}")
    print(f"WebBrowser: {get_web_browser()}")

with sync_playwright() as playwright:
    get_config_settings()