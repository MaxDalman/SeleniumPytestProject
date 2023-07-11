from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_promo_url(self):
        promo_url = self.browser.current_url
        assert "?promo=newYear" in promo_url, "Promo New Year url is not presented!"

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_be_correct_added_product(self):
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        added_to_basket = self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET)
        assert product_name == added_to_basket, "Product name != Product name in basket!"

    def should_be_correct_basket_price(self):
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.is_element_present(*ProductPageLocators.BASKET_PRICE)
        assert product_price != basket_price, "Product price == basket price!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"