import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import Checkout
import Expectedprice
import Login

class TestCreate(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_create_user(self):
        driver = self.driver
        Login.Positive(driver)
        driver.find_element(By.NAME,'login-button').click()
        time.sleep(2)
        driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
        time.sleep(2)
        driver.find_element(By.ID,'shopping_cart_container').click()
        time.sleep(2)
        driver.find_element(By.ID,'checkout').click()
        expected_price = Expectedprice
        print('$29.99')
        Checkout.checkout(driver)
        time.sleep(2)

unittest.main()

    