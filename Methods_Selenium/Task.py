import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    price =  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result = calc(int(x))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
