from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class HeaderPage:
    menuBtn = (By.ID, "react-burger-menu-btn")
    allItemBtn = (By.ID, "inventory_sidebar_link")
    aboutBtn = (By.ID, "about_sidebar_link")
    logoutBtn = (By.ID, "logout_sidebar_link")
    resetAppBtn = (By.ID, "reset_sidebar_link")
    shoppingCart = (By.CLASS_NAME, "shopping_cart_link")

    isLogout = False

    def __init__(self, driver):
        self.driver = driver

    def isLoggedOut(self):
        self.isLogout = not self.isLogout
        return  self.isLoggedOut
    
    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menuBtn)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logoutBtn)
        ).click()
        self.isLoggedOut()
        assert self.isLogout == True


