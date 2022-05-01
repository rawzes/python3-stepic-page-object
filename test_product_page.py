from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
links[7] = pytest.param(links[7], marks=pytest.mark.xfail(reason='Known issue mark'))


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_be_success_message()
    product_page.should_be_correct_item_name()
    product_page.should_be_correct_basket_value()


@pytest.mark.xfail(reason='Known issue mark')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='Known issue mark')
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()

