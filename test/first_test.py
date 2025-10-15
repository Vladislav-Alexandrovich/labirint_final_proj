import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from pages.AuthPage import AuthPage


def first_test():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.implicitly_wait(5)
    browser.maximize_window

    auth_page = AuthPage(browser)
    auth_page.go()
    time.sleep(5)