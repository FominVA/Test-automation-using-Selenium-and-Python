import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий



def test_move_to_el(driver):
    action = ActionChains(driver)  # Создаем обьект action
    driver.get("https://demoqa.com/menu")

    STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
    STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
    STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

    STEP_1 = driver.find_element(*STEP_1_LOCATOR)
    STEP_2 = driver.find_element(*STEP_2_LOCATOR)
    STEP_3 = driver.find_element(*STEP_3_LOCATOR)

    action.move_to_element(STEP_1).move_to_element(STEP_2).click(STEP_3).perform()
    time.sleep(5)