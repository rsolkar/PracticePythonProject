from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "//input[@id='Password']").clear()
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

act_title = driver.title
expe_title = ("Dashboard / nopCommerce administration")

if act_title == expe_title:
    print("Test Passed")
else:
    print("Test Failed")

driver.close()
