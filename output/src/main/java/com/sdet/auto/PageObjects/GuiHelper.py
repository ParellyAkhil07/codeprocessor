
import playwright.sync_api as pw

class GuiHelper:
    @staticmethod
    def openWebBrowser():
        with pw.sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()

    @staticmethod
    def closeWebBrowser():
        browser.close()