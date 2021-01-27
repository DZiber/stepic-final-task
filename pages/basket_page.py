from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket link is not present"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products in basket is present, but should not be"

    def should_be_message_about_emptiness(self, expected_message):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTINESS), \
           "Message about empty basket is not present"
        actual_message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTINESS).text
        assert actual_message == expected_message, "Wrong book name!"
