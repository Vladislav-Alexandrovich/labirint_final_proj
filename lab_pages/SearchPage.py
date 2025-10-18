"""В этом классе хранятся методы для работы с поиском"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from creds import base_url


class SearchPage:
    @allure.step("ui.открытие бразера")
    def __init__(self, driver: WebDriver) -> None:
        """открываем браузер"""
        self.__driver = driver
        self.__driver.get(base_url)

    @allure.step("ui.передача куки")
    def put_cookie(self):
        """прописываем куки"""
        cookie = {'name': 'cookie_policy', 'value': '1'}
        self.__driver.add_cookie(cookie)
        self.__driver.refresh()

    @allure.step("Определение количества товаров в выкладке поиска")
    def goods_counter(self):
        """ищем кнопки добавления в корзину"""
        put_in_cart_button = self.__driver.find_elements(
            By.CSS_SELECTOR, '[data-carttext]')
        number_of_items = len(put_in_cart_button)
        return int(number_of_items)
