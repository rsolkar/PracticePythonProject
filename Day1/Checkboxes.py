from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
driver.implicitly_wait(15)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Method 1
for checkbox in checkboxes:
    weekday = checkbox.get_attribute('id')
    if weekday == "monday":
        checkbox.click()
        print("Checkbox selected")

'''
# Method 2 - If you want to select all checkboxes
for i in range(len(checkboxes)):
    checkboxes[i].click()

# Method 3 - If you want to select specific checkboxes you want to select checkboxes from 6 to 7
How many elements you want to select - If 2 then use 2
for i in range(len(checkboxes)-2, checkboxes):
    checkboxes[i].click()
'''



