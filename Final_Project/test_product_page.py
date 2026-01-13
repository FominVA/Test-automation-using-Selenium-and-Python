import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage

params = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]

@pytest.mark.parametrize('param', params)
def test_guest_can_add_product_to_basket(browser, param):
    product_page = ProductPage(browser, param)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_grocery()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()
    product_page.book_name_on_page()
    product_page.true_cost_of_book()

@pytest.mark.parametrize('param', params)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, param):
    product_page = ProductPage(browser, param)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_grocery()
    product_page.solve_quiz_and_get_code()
    product_page.is_not_element_present()

@pytest.mark.parametrize('param', params)
def test_guest_cant_see_success_message(browser, param):
    product_page = ProductPage(browser, param)
    product_page.open()
    product_page.should_be_product_page()
    product_page.is_not_element_present()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
    login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    login_page = LoginPage(browser,login_link)
    login_page.should_be_login_page()

