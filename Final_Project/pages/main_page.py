from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_basket(self):
        current_URL = self.browser.current_url
        print('Проверка URL прошла')
        assert '/basket/' in current_URL

    def should_be_empty_basket(self):
        empty_basket_text = self.browser.find_element(*MainPageLocators.EMPTY_BASKET)
        assert "Your basket is empty." in empty_basket_text.text



