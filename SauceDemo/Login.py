import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def Positive(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.NAME,'user-name').send_keys('standard_user')
    time.sleep(2)
    driver.find_element(By.NAME,'password').send_keys('secret_sauce')
   