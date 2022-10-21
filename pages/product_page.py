from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def should_be_sum_basket(self, prices):
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text[14:][:-12] == prices, "Sum basket is wrong"

    def should_be_added_product(self, prod_name):
        assert self.browser.find_element(*ProductPageLocators.NAME_ADDED_PRODUCT).text == prod_name, "Name product is wrong"
        assert self.browser.find_element(*ProductPageLocators.BASKET_ADDED_TEXT).text == \
               prod_name + ' has been added to your basket.', \
            "Basket added text is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ADDED_TEXT), \
            "Success message is presented, but should not be"