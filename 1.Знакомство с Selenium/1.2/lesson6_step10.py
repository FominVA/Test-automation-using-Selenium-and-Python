from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    data = {'first_name': 'Slavik', 'second_name': 'Fomin', 'email': 'FominVA@yandex.ru'}
    required_fields = browser.find_elements(By.CSS_SELECTOR,"input.form-control.first, input.form-control.second, input.form-control.third")
    # Используем специфичные селекторы на основе классов, которые различаются для обязательных полей
    assert len(required_fields) == 3, f"Ожидалось 3 обязательных поля ввода, найдено {len(required_fields)}"
    print("Тест провален: Найдено не 3 обязательных поля ввода.")
    # 1. First name (используем селектор по классу, который уникален для этого поля)
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

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    # Проверка количества найденных элементов не имеет смысла в этом контексте, так как мы их не используем для заполнения.
    # Если вы хотите проверить, что всего 4 поля ввода (3 обязательных + 1 файл), это нужно делать отдельно.
    # elements = browser.find_elements(By.CSS_SELECTOR, '.first_block input')
    # assert len(elements) == 3 # Это будет неверно, так как есть 4 инпута.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()