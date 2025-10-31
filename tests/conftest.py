from selenium import webdriver

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from pages.login_page  import LoginPage

import random
import pytest


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions() 
    options.add_argument("--disable-notifications") 
    options.add_argument("--disable-popup-blocking") 
    options.add_argument("--incognito") 
    options.add_argument("--no-first-run") 
    options.add_argument("--no-service-autorun") 
    options.add_argument("--password-store=basic") 
    options.add_argument("--disable-save-password-bubble") 
    options.add_argument("--disable-infobars") 
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.openBrowser()
    login_page.loginPage("standard_user", "secret_sauce") 
    yield driver

@pytest.fixture(scope="session")
def selected_products():
    allProducts = ['backpack', 'bike-light', 'bolt-t-shirt', 'fleece-jacket', 'onesie']
    selected = random.sample(allProducts, 2)
    print("Selected products: ", selected)
    return selected