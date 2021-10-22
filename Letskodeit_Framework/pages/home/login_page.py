from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        loginLink = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys("n3g@mail.ru")

        passwordField = self.driver.find_element(By.ID, "password")
        passwordField.send_keys("volcom99")

        loginButton = self.driver.find_element(By.NAME, "commit")
        loginButton.click()
