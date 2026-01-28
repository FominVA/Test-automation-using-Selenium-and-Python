import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def test_dropdown_options(driver):
    DROPDOWN_LOCATOR = ('xpath', '//select[@id="dropdown"]')
    driver.get("http://the-internet.herokuapp.com/dropdown")
    DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
    DROPDOWN_LIST = DROPDOWN.options
    for el in DROPDOWN_LIST:
        print(el)

def test_dropdown_select_by_visible_text(driver):
    DROPDOWN_LOCATOR = ('xpath', '//select[@id="dropdown"]')
    driver.get("http://the-internet.herokuapp.com/dropdown")
    DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
    DROPDOWN.select_by_visible_text("Option 2")
    time.sleep(5)

def test_dropdown_select_by_value(driver):
    DROPDOWN_LOCATOR = ('xpath', '//select[@id="dropdown"]')
    driver.get("http://the-internet.herokuapp.com/dropdown")
    DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
    DROPDOWN.select_by_value("1")
    time.sleep(5)