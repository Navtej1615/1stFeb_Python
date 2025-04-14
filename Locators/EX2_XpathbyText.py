import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
#driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()