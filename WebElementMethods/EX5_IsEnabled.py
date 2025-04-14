import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
Button=driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")
if Button.is_enabled():
    print("Button is enabled")
    Button.click()
else:
    print("Button is not enabled")