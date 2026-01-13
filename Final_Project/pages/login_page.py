from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_URL = self.browser.current_url
        print('Проверка URL прошла')
        assert 'accounts/login/' in current_URL

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print('Проверка формы логина прошла')
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print('Проверка формы регистрации прошла')
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)

