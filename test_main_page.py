from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()
        login_page.should_be_register_form()
        login_page.should_be_login_url()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
