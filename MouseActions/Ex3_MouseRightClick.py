import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
cartelement=driver.find_element(By.XPATH,"//a[text()='Cart']");
act=ActionChains(driver)
#act.move_to_element(Cartelement).perform()
act.context_click(cartelement).perform()
time.sleep(4)