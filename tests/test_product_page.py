import pytest

import pages.links as links
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.check_success_adding_message("Coders at Work")
    product_page.check_cart_total_message("19.99")


@pytest.mark.xfail(reason="Failed according to task")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, links.PRODUCT_PAGE_LINK)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, links.PRODUCT_PAGE_LINK)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="Failed according to task")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, links.PRODUCT_PAGE_LINK)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, links.PRODUCT_FOR_LOGIN_LINK)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, links.PRODUCT_FOR_LOGIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, links.PRODUCT_PAGE_LINK)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, links.PRODUCT_PAGE_LINK)
    basket_page.should_be_basket_url()
    basket_page.should_not_be_products()
    basket_page.should_be_message_about_emptiness("Your basket is empty. Continue shopping") \
        # only english: https://stepik.org/lesson/201964/step/10?auth=login&discussion=1057515&reply=1057527&unit=176022
