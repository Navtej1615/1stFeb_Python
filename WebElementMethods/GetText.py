import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
UN=driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']")
UN.send_keys("Navtej")
Text=UN.get_attribute("Value")
print(Text)
time.sleep(2)
NewAccount=driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").text
print(NewAccount)