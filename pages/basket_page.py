from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FULL_BASKET), \
            "Basket is not empty, but should be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Text is not presented, but should be"