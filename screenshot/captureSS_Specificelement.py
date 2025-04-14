import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']").screenshot("F:\PythonAutomationDailyNotes\ScreenShots\img1.png")