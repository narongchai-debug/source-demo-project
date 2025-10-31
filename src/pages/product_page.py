from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
    
    def addToCart(self, product_id):
        item = (By.ID, f"add-to-cart-sauce-labs-{product_id}")

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(item)
        ).click()
