import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
time.sleep(2)
#step1:identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']")

#step 2:Create object of select class
s=Select(month)
#3 -call select class method
#s.select_by_visible_text("Oct")
#s.select_by_value("5")
#s.select_by_index(11)
#s.deselect_all()
result=s.is_multiple
print(result)
time.sleep(2)
