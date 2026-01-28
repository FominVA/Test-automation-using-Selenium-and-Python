from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = func(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.ID,'answer')
    answer.send_keys(result)
    checkbox = browser.find_element(By.ID,'robotCheckbox')
    checkbox.click()
    rb = browser.find_element(By.ID, 'robotsRule')
    rb.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()