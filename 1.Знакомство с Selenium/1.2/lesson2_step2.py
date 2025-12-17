
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'
def func_sum(num1, num2):
    return str(int(num1)+int(num2))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = func_sum(num1, num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    time.sleep(100)
    button.click()
except:
    time.sleep(100)
    browser.quit()
