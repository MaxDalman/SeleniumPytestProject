from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'Посмотреть корзину')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product_main']/h1[1]")
    ADDED_TO_BASKET = (By.XPATH, "//div[@class='alertiner']/strong[1]")

    PRODUCT_PRICE = (By.XPATH, "//div[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertiner']/p/strong[1]")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    FULL_BASKET = (By.CSS_SELECTOR, ".col-sm-6")
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'пуста')]")