import time

from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
driver.get("https://www.facebook.com/")
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
