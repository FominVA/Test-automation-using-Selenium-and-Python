import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element(By.ID, "treasure")
    x_element = treasure.get_attribute("valuex")
    y = calc(x_element)
    input_text = browser.find_element(By.ID, 'answer')
    input_text.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()