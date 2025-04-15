import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/droppable.php")
source=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
destination=driver.find_element(By.XPATH,"//p[text()='Drop here']")

act= ActionChains(driver)
act.drag_and_drop(source,destination).perform()
act.move_to_element(source).click_and_hold().move_to_element(destination).release().perform()
time.sleep(5)
