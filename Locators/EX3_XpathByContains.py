#Attribute----->//tagname[contains(@attributeName,'partial attribute value')]

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[contains(@placeholder, 'Email address')]").send_keys("Navtej@1234")
