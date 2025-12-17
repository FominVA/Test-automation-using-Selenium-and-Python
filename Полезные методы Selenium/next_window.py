import os
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'

    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn.btn-primary')
    button.click()
    second_window = browser._switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result = calc(int(x))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()