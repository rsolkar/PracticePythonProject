import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    assert driver.title == "Google", "Test Failed"
    driver.close()

def test_edge():
    driver = webdriver.Edge()
    driver.get("https://www.google.com/")
    assert driver.title == "ABC", "Test Failed"
    driver.close()



