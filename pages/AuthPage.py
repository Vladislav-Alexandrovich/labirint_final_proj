from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.labirint.ru/"
        self.__driver = driver

    
    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys(email)