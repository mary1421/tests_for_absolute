from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_basket_empty_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text == \
               'Your basket is empty. Continue shopping', \
            "Basket empty message is not presented or is wrong, but should be"
