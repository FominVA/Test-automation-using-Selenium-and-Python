from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.buy_button_on_page()


    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        current_URL = self.browser.current_url
        print('Проверка URL прошла')
        assert "?promo=offer" in current_URL

    def buy_button_on_page(self):
        button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        assert "Добавить в корзину" in button.text

    def add_to_grocery(self):
        button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        button.click()


    def book_name_on_page(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_grocery = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_GROCERY)
        assert book_name_in_grocery.text == book.text

    def true_cost_of_book(self):
        book_cost = self.browser.find_element(*ProductPageLocators.BOOK_COST)
        book_cost_in_grocery = self.browser.find_element(*ProductPageLocators.BOOK_COST_IN_GROCERY)
        assert book_cost.text == book_cost_in_grocery.text

    def should_be_product_title_in_message(self): # проверка успешного добавления товара
        product_title = self.find_element_ex_wait(Locators.PRODUCT_TITLE).text
        successful_adding_message = self.find_element_ex_wait(Locators.MESSAGE_SUCCESSFUL_ADDING).text
        assert product_title in successful_adding_message, \
            "Message of successful adding product is not correct"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
