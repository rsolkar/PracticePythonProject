# displayed, enabled, selected
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

time.sleep(1)

el1 = driver.find_element(By.XPATH, "//input[@id='Email']")
print("Element is displayed:", el1.is_displayed())
print("Element is enabled:", el1.is_enabled())

el2 = driver.find_element(By.XPATH, "//input[@id='RememberMe']")
print("Element is selected:", el2.is_selected())

driver.close()

