import pytest

import pages.links as links
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPag():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, links.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, links.MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, links.MAIN_PAGE_LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, links.PRODUCT_PAGE_LINK)
        basket_page.should_be_basket_url()
        basket_page.should_not_be_products()
        basket_page.should_be_message_about_emptiness("Your basket is empty. Continue shopping") \
            # only english: https://stepik.org/lesson/201964/step/10?auth=login&discussion=1057515&reply=1057527&unit=176022
