
from playwright.sync_api import Page
from playwright.sync_api import BrowserContext
from playwright.sync_api import Browser
from playwright.sync_api import chromium
import json

def basic_accessibility_check(page: Page, browser_context: BrowserContext, browser: Browser):
    script_url = "https://unpkg.com/axe-core@4.3.2/axe.min.js"
    response_json = page.evaluate(f"""() => {{
        return new Promise(async (resolve) => {{
            const axe = await import('{script_url}');
            const result = await axe.default(document);
            resolve(result);
        }});
    }}""")
    violations = json.loads(response_json)["violations"]

    if len(violations) == 0:
        print("PASS: basicAccessibilityCheck | No violations found.")
    else:
        print("FAIL: " + IoLibrary.getTestName() + " " + AXE.report(violations))