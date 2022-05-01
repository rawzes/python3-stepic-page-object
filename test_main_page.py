from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    login_page.should_be_login_url()

