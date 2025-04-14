import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
try:
 RadioButton=driver.find_element(By.NAME,"sex").is_selected()
 print(RadioButton)
except NoSuchElementException:
 print("Element not found")
