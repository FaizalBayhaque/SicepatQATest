import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

   
def checkout(driver):
    driver.find_element(By.NAME,'firstName').send_keys('John')
    driver.find_element(By.NAME,'lastName').send_keys('Doe')
    driver.find_element(By.NAME,'postalCode').send_keys('42436')
