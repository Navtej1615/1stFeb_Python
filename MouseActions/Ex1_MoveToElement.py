import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
loginelement=driver.find_element(By.XPATH,"//span[text()='Login']")
act=ActionChains(driver)
act.move_to_element(loginelement).perform()
driver.find_element(By.XPATH,"//li[text()='Gift Cards']").click()
time.sleep(5)