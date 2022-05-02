from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    BASKET_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn-default')


class BasketPageLocators:
    EMPTY_BASKET_PRICE = (By.XPATH, '//*[@id="content_inner"]/p')
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p/a')
