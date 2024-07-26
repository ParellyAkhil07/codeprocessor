
from playwright.sync_api import Page

class ConfigSettings:
    web_url = ""
    web_browser = ""

    def get_web_url(self):
        return self.web_url

    def set_web_url(self, web_url):
        self.web_url = web_url

    def get_web_browser(self):
        return self.web_browser

    def set_web_browser(self, web_browser):
        self.web_browser = web_browser

    def get_config_settings(self):
        property = {}
        prop_file_name = "config.properties"
        with open(prop_file_name) as f:
            for line in f:
                key, value = line.split("=")
                property[key] = value

        self.set_web_url(property["webUrl"])
        self.set_web_browser(property["webBrowser"])

        print("Test Config Settings")
        print(f"WebUrl: {self.get_web_url()}")
        print(f"WebBrowser: {self.get_web_browser()}")