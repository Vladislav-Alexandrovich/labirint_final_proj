import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from creds import base_url


@pytest.fixture
def browser():
    """ Здесь собрана фикстура, которая передает брузер:
открывает страницу и вставляет куки"""
    with allure.step("Открыть настроенный браузер"):
        browser = webdriver.Firefox(service=FirefoxService
                                    (GeckoDriverManager().install()))
        browser.implicitly_wait(10)
        browser.maximize_window()
        browser.get(base_url)

        cookie = {'name': 'cookie_policy', 'value': '1'}
        browser.add_cookie(cookie)
        # browser.refresh()

        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
