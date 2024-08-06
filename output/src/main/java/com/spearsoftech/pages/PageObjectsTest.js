import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.Assert.assertEquals;

public class PageObjectsTest {
    private WebDriver driver;
    private PageObjects pageObjects;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
        pageObjects = new PageObjects(driver);
    }

    @After
    public void tearDown() {
        driver.quit();
    }

    @Test
    public void testRegisterLink() {
        driver.get("https://demo.nopcommerce.com/");
        pageObjects.getRegisterLink().click();
        assertEquals("Register", driver.getTitle());
    }

    @Test
    public void testRegisterBtn() {
        driver.get("https://demo.nopcommerce.com/register");
        pageObjects.getRegisterBtn().click();
        assertEquals("Your registration completed", pageObjects.getRegistrationSuccessMsg().getText());
    }