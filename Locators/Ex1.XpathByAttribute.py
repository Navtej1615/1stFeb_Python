import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']").send_keys("Navtej@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='pass']").send_keys("Test@123")
time.sleep(2)
Button=driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']")
if Button.is_enabled():
    print("Button is enabled")
    Button.click()
else:
    print("Button is not enabled")

#driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Navtej")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Patil")
dropdown_element = driver.find_element(By.ID, "day")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("2")
dropdown_element1 = driver.find_element(By.ID, "month")
dropdown1 = Select(dropdown_element1)
dropdown1.select_by_visible_text("Oct")
dropdown_element2 = driver.find_element(By.ID, "year")
dropdown2 = Select(dropdown_element2)
dropdown2.select_by_visible_text("1996")
driver.find_element(By.NAME,"sex").click()
driver.find_element(By.NAME,"reg_email__").send_keys("123456789")
driver.find_element(By.NAME,"reg_passwd__").send_keys("Test@123")
time.sleep(2)
driver.back()