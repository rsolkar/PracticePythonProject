from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
url = driver.current_url
print(url)
title1 = driver.title
print(title1)
pg_source = driver.page_source
print(pg_source)
