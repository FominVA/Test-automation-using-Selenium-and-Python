import os
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Slavik')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Fomin')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('FominVA@yandex.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
