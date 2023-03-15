from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\Rutuja Solkar\Desktop\Drivers\Chrome\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click

act_title = driver.title
expec_title = "OrangeHRM"

if act_title == expec_title:
    print("Login Test Passed")
else:
    print("Test Failed")

driver.close()

'''Another way to write Selenium4
from selenium.webdriver.chrome.service import service
serv_obj=Service("C:\Users\Rutuja Solkar\Desktop\Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

If you have added the drivers to the script then no need to even define the driver path

driver=webdriver.Chrome()

'''
