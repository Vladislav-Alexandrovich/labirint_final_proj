import pytest
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser

    browser.quit()