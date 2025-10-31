from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    goToCart = (By.CLASS_NAME, "shopping_cart_link")
    checkoutButton = (By.ID, "checkout")
    continueButton = (By.ID, "continue")
    finishButton = (By.ID, "finish")
    localFirstName = (By.ID, "first-name")
    localLastName = (By.ID, "last-name")
    localPostalCode = (By.ID, "postal-code")
    
    backToHome = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver

    def removeItems(self, items): 
        removeBtn = (By.ID, f"remove-sauce-labs-{items}")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(removeBtn)
        ).click()
 
        
    def checkOutItems(self, firstname, lastname, postalcode):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.goToCart)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkoutButton)
        ).click()

        locatorFirstName =  WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.localFirstName)
        )
        locatorLastName = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.localLastName)
        )
        locatorPostalCode = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.localPostalCode)
        )

        #Clear information
        locatorFirstName.clear()
        locatorLastName.clear()
        locatorPostalCode.clear()

        #Input information
        locatorFirstName.send_keys(firstname)
        locatorLastName.send_keys(lastname)
        locatorPostalCode.send_keys(postalcode)

        #Continue Checkout
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continueButton)
        ).click()
        assert "Overview" in self.driver.page_source

        #Finish checkout
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finishButton)
        ).click()
        assert "Thank you for your order!" in self.driver.page_source

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backToHome)
        ).click()
        assert "inventory" in self.driver.current_url

