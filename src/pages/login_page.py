from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class LoginPage:
    inputUsername = (By.ID, "user-name")
    inputPassword = (By.ID, "password")
    loginButton = (By.ID, "login-button")
    BASE_URL = "https://www.saucedemo.com"

    isLogin = False


    def __init__(self, driver):
        self.driver = driver


    def openBrowser(self):
        self.driver.get(self.BASE_URL)

    def isLoggedIn(self):
        self.isLogin = not self.isLogin
        return self.isLoggedIn

    def loginPage(self, username, password):
        locatorUsername =  WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.inputUsername)
        )

        locatorPassword = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.inputPassword)
        )
        #Clear input data
        locatorUsername.clear()
        locatorPassword.clear()

        #Input username, password
        locatorUsername.send_keys(username)
        locatorPassword.send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.loginButton).click()
        self.isLoggedIn()
        assert self.isLogin == True

