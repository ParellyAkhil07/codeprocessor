public void testRegisterUser() {
    String email = faker.internet().emailAddress();
    String password = "";
    pageActions.registerUser(email, password);
    Assert.assertTrue(pageActions.isUserLoggedIn());
}

@Test
public void testLoginUser() {
    String email = faker.internet().emailAddress();
    String password = "";
    pageActions.registerUser(email, password);
    pageActions.logOutUser();
    pageActions.loginUser(email, password);
    Assert.assertTrue(pageActions.isUserLoggedIn());
}

@Test
public void testLogoutUser() {
    String email = faker.internet().emailAddress();
    String password = "";
    pageActions.registerUser(email, password);
    pageActions.logOutUser();
    Assert.assertTrue(pageActions.isUserLoggedOut());