import static org.junit.Assert.assertNotNull;

public class PageObjectsTest {

    @Test
    public void testRegisterLinkExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getRegisterLink());
    }

    @Test
    public void testRegisterBtnExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getRegisterBtn());
    }

    @Test
    public void testLogInLinkExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getLogInLink());
    }

    @Test
    public void testFirstNameTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getFirstNameTxt());
    }

    @Test
    public void testGenderMaleExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getGenderMale());
    }

    @Test
    public void testLastNameTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getLastNameTxt());
    }

    @Test
    public void testDobDayExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getDobDay());
    }

    @Test
    public void testDobMonthExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getDobMonth());
    }

    @Test
    public void testDobYearExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getDobYear());
    }

    @Test
    public void testEmailTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getEmailTxt());
    }

    @Test
    public void testComputersLinkExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getComputersLink());
    }

    @Test
    public void testCompanyTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getCompanyTxt());
    }

    @Test
    public void testPasswordTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getPasswordTxt());
    }

    @Test
    public void testConfirmPasswordTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getConfirmPasswordTxt());
    }

    @Test
    public void testRegistrationSuccessMsgExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getRegistrationSuccessMsg());
    }

    @Test
    public void testContinueBtnExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getContinueBtn());
    }

    @Test
    public void testLogOutLinkExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getLogOutLink());
    }

    @Test
    public void testEmailLoginTxtExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getEmailLoginTxt());
    }

    @Test
    public void testLoginBtnExists() {
        PageObjects pageObjects = new PageObjects(driver);
        assertNotNull(pageObjects.getLoginBtn());
    }