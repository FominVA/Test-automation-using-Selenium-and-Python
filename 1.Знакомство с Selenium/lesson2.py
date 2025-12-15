
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
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    result = func_sum(num1, num2)
    print(result)

except:
    time.sleep(10)
    browser.quit()