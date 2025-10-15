import Allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def auth_test(browser):

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as()