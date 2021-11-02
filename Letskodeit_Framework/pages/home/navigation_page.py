import logging
from lets_kode_it.Letskodeit_Framework.base.selenium_driver import SeleniumDriver
from lets_kode_it.Letskodeit_Framework.utilities import custom_logger as cl
from lets_kode_it.Letskodeit_Framework.base.basepage import BasePage

# class LoginPage(SeleniumDriver):
class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//img[@alt='n3g@mail.ru']"
    _home = "//a[@class='navbar-brand header-logo']"

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses,locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="xpath")
