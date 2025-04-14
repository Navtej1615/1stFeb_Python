import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
option=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
s=Select(option)
text=s.first_selected_option.text
print(text)

