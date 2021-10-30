import logging
from lets_kode_it.Letskodeit_Framework.base.selenium_driver import SeleniumDriver
from lets_kode_it.Letskodeit_Framework.utilities import custom_logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "email"
    _password_field = "password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@alt='n3g@mail.ru']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Your email or password is incorrect')]", locatorType="xpath")
        return result

    def verifyTitle(self):
        if "Let's Kode It" in self.getTitle():
        #if "Google" in self.getTitle():
            return True
        else:
            return False

