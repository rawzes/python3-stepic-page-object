from pages.product_page import ProductPage
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
    product_page.should_be_correct_basket_value()
