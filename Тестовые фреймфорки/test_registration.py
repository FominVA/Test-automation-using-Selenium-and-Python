from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_registration1(browser):
    link = "https://suninjuly.github.io/registration1.html"
    browser.get(link)
    data = {'first_name': 'Slavik', 'second_name': 'Fomin', 'email': 'FominVA@yandex.ru'}
    required_fields = browser.find_elements(By.CSS_SELECTOR,".first_block .form-group.first_class input.form-control.first, .first_block .form-group.second_class input.form-control.second, .first_block .form-group.third_class input.form-control.third")

    assert len(required_fields)== 3, f"Ожидалось 3 обязательных поля ввода, найдено {len(required_fields)}"

    first_name_field = browser.find_element(By.CSS_SELECTOR, "input.form-control.first")
    first_name_field.send_keys(data['first_name'])

     # 2. Last name
    second_name_field = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
    second_name_field.send_keys(data['second_name'])

     # 3. Email
    email_field = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
    email_field.send_keys(data['email'])

        # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

        # находим элемент, содержащий текст
    wait = WebDriverWait(browser, 10)
    welcome_text_elt = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    expected_text = "Congratulations! You have successfully registered!"
    assert welcome_text==expected_text, f"Ожидаемый текст '{expected_text}' не совпал с фактическим '{welcome_text}'"


