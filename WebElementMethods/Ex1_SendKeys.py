import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
#appr 1
#driver.find_element(By.XPATH,"//input[contains(@placeholder, 'Email address')]").send_keys("Navtej@1234")

#appr2
EmailAd=driver.find_element(By.XPATH,"//input[contains(@placeholder, 'Email address')]")
EmailAd.send_keys("TestEmail@gmail.com")
time.sleep(2)