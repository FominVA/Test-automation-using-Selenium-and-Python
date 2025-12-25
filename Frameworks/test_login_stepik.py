import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def answer():
    return str(math.log(int(time.time())))
Links =['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                              'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                              'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                              'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']
LOGIN_BUTTON = (By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')


def login(self, browser, link):
    browser.get(f'{link}')
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    login = browser.find_element(By.CSS_SELECTOR, 'input#id_login_email').send_keys("пфывафывап")
    password = browser.find_element(By.CSS_SELECTOR, 'input#id_login_password').send_keys("пвапывап")
    entry_button = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader ').click()

class TestFindElement:
    @pytest.mark.parametrize('link', Links)
    def test_from_answer(self, browser, link):
        login(self, browser, link)
        WebDriverWait(browser, 10).until_not(EC.presence_of_all_elements_located(LOGIN_BUTTON))

        WebDriverWait(browser, 20, 0.5).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        ).send_keys(answer())

        send_button = WebDriverWait(browser, 20, 1.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        send_button.click()

        time.sleep(5)
        correct = browser.find_element(By.CSS_SELECTOR,'p.smart-hints__hint')
        correct_text = correct.text
        assert correct_text == "Correct!"
