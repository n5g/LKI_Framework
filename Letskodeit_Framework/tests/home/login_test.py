
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lets_kode_it.Letskodeit_Framework.pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
        baseURL = "https://letskodeit.teachable.com/"
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver) #создал переменую lp  и унаследовал ее от LoginPage + сделал импорт файла
        lp.login("n3g@mail.ru", "volcom99") #  в функцию login передал почту и пароль
        result = lp.verifyLoginSuccessful()

        assert result == True

        driver.quit()


