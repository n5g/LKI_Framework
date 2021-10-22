import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from lets_kode_it.Letskodeit_Framework.pages.home.login_page import LoginPage
import unittest
import pytest

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

        userIcon = driver.find_element(By.XPATH, "//img[@alt='n3g@mail.ru']")
        if userIcon is not None:
            print("Login successful")
        else:
            print("Login Failed")

        driver.quit()


