import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def browser():
    with allure.step("Открыть настроенный браузер"):
        browser = webdriver.Firefox(service=FirefoxService
                                    (GeckoDriverManager().install()))
        browser.implicitly_wait(5)
        browser.maximize_window()
        
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()