import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")
time.sleep(2)
driver.save_screenshot("F:\PythonAutomationDailyNotes\ScreenShots\img1.png")