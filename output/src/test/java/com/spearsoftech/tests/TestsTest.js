import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class Tests extends BaseFactory {

    protected BasePage basePage;
    protected PageObjects pageObjects;
    protected PageActions pageActions;

    @BeforeMethod
    public void setUpObjects() {

        initializeDriver();
        navigateToURL("https://demo.nopcommerce.com/");
        basePage = new BasePage(getDriver());
        pageObjects = new PageObjects(getDriver());
        pageActions = new PageActions(getDriver());
    }

    @Test (priority = 0)
    public void testRegisterFunctionality() {

        pageActions.registerUser(BasePage.email,BasePage.pwd);
        basePage.explicitWait(30).until(ExpectedConditions.visibilityOf(pageActions.getRegistrationSuccessMsg()));
        Assert.assertEquals(pageObjects.getRegistrationSuccessMsg().getText(),"Your registration completed","First Name field is not displayed");
    }

    @Test (priority = 1)
    public void testLogoutFunctionality() {

        pageActions.loginUser(BasePage.email,BasePage.pwd);
        pageActions.logOutUser();
        basePage.explicitWait(30).until(ExpectedConditions.visibilityOf(pageActions.getLogInLink()));
        Assert.assertTrue(pageObjects.getLogInLink().isDisplayed(), "Log Out link is not displayed");
    }