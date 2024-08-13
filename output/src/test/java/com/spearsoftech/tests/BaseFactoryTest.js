import static org.testng.Assert.assertEquals;

public class BaseFactoryTest {
    @Test
    public void testInitializeDriver() {
        BaseFactory.initializeDriver();
        assertEquals(BaseFactory.getDriver().getClass().getName(), "org.openqa.selenium.chrome.ChromeDriver");
    }

    @Test
    public void testNavigateToURL() {
        BaseFactory.initializeDriver();
        BaseFactory.navigateToURL("https://www.google.com");
        assertEquals(BaseFactory.getDriver().getCurrentUrl(), "https://www.google.com/");
    }