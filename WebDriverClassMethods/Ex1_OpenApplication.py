import time

from selenium import webdriver
driver= webdriver.Chrome()

driver.get("https://www.naukri.com/")
#driver.get("https://www.google.com/")
time.sleep(5)
TitleValue=driver.title
print(TitleValue)

driver.close()
