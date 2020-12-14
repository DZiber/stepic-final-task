from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_adding_to_basket(self):
        expected_text = "The shellcoder\'s handbook has been added to your basket.\n" \
                        "Your basket now qualifies for the Deferred benefit offer offer.\n" \
                        "Your basket total is now £9.99"
        messages_text = self.browser.find_element(*ProductPageLocators.MESSAGES).text.replace("×\n", "").replace("\nView basket Checkout now", "")
        assert messages_text == expected_text, "Wrong message!"

