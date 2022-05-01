from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_be_success_message()
    product_page.should_be_correct_item_name()
    product_page.should_be_correct_basket_value()
    product_page.should_be_correct_basket_value()
