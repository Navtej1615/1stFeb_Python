import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")
dropdown=driver.find_element(By.XPATH,"//span[@class='mbsc-textfield-tags-placeholder mbsc-ios']")
s=Select(dropdown)
print(s.first_selected_option)
