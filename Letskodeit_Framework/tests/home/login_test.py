
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lets_kode_it.Letskodeit_Framework.pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    baseURL = "https://letskodeit.teachable.com/"
    driver.maximize_window()
    driver.implicitly_wait(3)
    lp = LoginPage(driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # self.lp.login("n3g@mail.ru", "volcom99") #  в функцию login передал почту и пароль
        self.lp.login(password="volcom99")

        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("n3g@mail.ru", "volcom")
        result = self.lp.verifyLoginFailed()
        assert result == True



