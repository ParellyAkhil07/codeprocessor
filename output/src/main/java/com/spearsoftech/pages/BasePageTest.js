    private BasePage basePage;

    @Before
    public void setUp() {
        // Create a new instance of the BasePage class
        basePage = new BasePage(driver);
    }

    @Test
    public void testSelectDropdownValue() {
        // Test the selectDropdownValue method
        WebElement dropdownElement = driver.findElement(By.id("dropdown-id"));
        basePage.selectDropdownValue(dropdownElement, "Option 1");
        Select select = new Select(dropdownElement);
        assertEquals("Option 1", select.getFirstSelectedOption().getText());
    }

    @Test
    public void testRandomMonth() {
        // Test the getRandomMonth method
        String randomMonth = basePage.getRandomMonth();
        List<String> months = Arrays.asList(
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
        );
        assertTrue(months.contains(randomMonth));
    }