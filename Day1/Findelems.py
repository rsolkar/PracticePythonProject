# Find elements one as well as whole list

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

time.sleep(1)

elements = driver.find_elements(By.XPATH, "//a")
print(elements[0].text)
print(elements[1].text)

for ele in elements:
    print(ele.text)

print("No of Links:", len(elements))

