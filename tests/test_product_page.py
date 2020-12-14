import pages.links as links
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, links.PRODUCT_PAGE_LINK)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_adding_to_basket()