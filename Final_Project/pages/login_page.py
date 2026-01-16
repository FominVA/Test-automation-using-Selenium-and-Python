from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver
import time

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

    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemail.org"
        password = "password1234567"
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM_REGISTRATE)
        email_form.send_keys(email)
        password_form1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_REGISTRATE)
        password_form1.send_keys(password)
        password_form2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_CONFIRM)
        password_form2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()