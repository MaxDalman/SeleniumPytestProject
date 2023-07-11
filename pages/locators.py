from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product_main']/h1[1]")
    ADDED_TO_BASKET = (By.XPATH, "//div[@class='alertiner']/strong[1]")

    PRODUCT_PRICE = (By.XPATH, "//div[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertiner']/p/strong[1]")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")