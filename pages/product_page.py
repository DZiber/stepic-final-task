from accessify import private

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def check_success_adding_message(self, expected_book_name):
        actual_book_name = self.get_bold_text(*ProductPageLocators.SUCCESS_MESSAGE)
        assert actual_book_name == expected_book_name, "Wrong book name!"

    def check_cart_total_message(self, expected_price):
        actual_price = self.get_bold_text(*ProductPageLocators.TOTAL_MESSAGE)
        assert actual_price[1:] == expected_price, "Wrong book price!" \
        # удаление первого символа для независимости локализации, можно удалить если проверка символа валюты необходима

    @private
    def get_bold_text(self, by, locator):
        return self.browser.find_element(by, locator).find_element_by_tag_name("strong").text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should disappear"
