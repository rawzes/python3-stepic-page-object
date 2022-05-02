from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        if "promo=offer" in self.browser.current_url:
            self.solve_quiz_and_get_code()

    def get_product_name(self, locator):
        return self.browser.find_element(*locator).text

    def get_product_price(self, locator):
        return str(self.browser.find_element(*locator).text).strip().split("£")[1]

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_be_correct_item_name(self):
        initial_name = self.get_product_name(ProductPageLocators.PRODUCT_PAGE_NAME)
        actual_name = self.get_product_name(ProductPageLocators.PRODUCT_NAME)
        assert initial_name == actual_name, "Wrong product name"

    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "Basket message is not displayed"

    def should_be_correct_basket_value(self):
        product_price = self.get_product_price(ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.get_product_price(ProductPageLocators.BASKET_PRICE)
        assert product_price == basket_price, "Basket price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE), "Success message is presented, but " \
                                                                                 "should not be "

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE), "Success message is presented, but " \
                                                                         "should not be"
