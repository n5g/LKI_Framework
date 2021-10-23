from selenium.webdriver.common.by import By
from lets_kode_it.Letskodeit_Framework.base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver): # импортировал кастомный класс  SeleniumDriver

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = "Login"
    _email_field = "email"
    _password_field = "password2"
    _login_button = "commit"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.PARTIAL_LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field )
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        # self.getLoginLink().click()
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        # self.getEmailField().send_keys(email)
        self.sendKeys(email, self._email_field)   # locatorType="id" locator ID по умолчанию

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
