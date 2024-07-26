
import axe_playwright

async def basic_accessibility_check(test_assert):
    results = await axe_playwright.inject()
    violations = results["violations"]

    if len(violations) == 0:
        print("PASS: basicAccessibilityCheck | No violations found.")
    else:
        test_assert.set_pass(False)
        print("FAIL: " + axe_playwright.report(violations))