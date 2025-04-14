import time

from selenium import webdriver
driver=webdriver.Chrome()
#webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(10)
actTitle=driver.title
print(actTitle)
if actTitle=="Google":
    print("Pass")
else:
    print("Fail")

print(driver.current_url)