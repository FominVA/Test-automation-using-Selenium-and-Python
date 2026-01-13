from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocators():
    BUY_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    BOOK_COST = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_NAME_IN_GROCERY = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_COST_IN_GROCERY = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")