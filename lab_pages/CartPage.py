""" В этом классе хранятся методы для добавления товаров в корзину
и для работы с самой корзиной"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import base_url


class CartPage:
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

    @allure.step("ui.проверка пустой корзины")
    def check_empty_cart(self):
        """проверяем что корзина пустая"""
        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-personal-e-link[href="/cart/"]'
            ).click()
        empty_cart_message = self.__driver.find_element(
            By.XPATH, "//span[contains(text(), 'Ваша корзина пуста')]").text
        return empty_cart_message

    @allure.step("ui.добавление товара в корзину")
    def put_item_in_cart(self):
        """добавляем любую книгу в корзину"""
        self.__driver.find_element(By.XPATH,
                                   '(//*[@data-carttext])[1]').click()
        self.__driver.find_element(By.CSS_SELECTOR,
                                   '.b-header-b-personal-e-link[href="/cart/"]'
                                   ).click()
        cart_result = self.__driver.find_element(By.ID,
                                                 'basket-default-prod-count2'
                                                 ).text
        books_in_cart = cart_result.split()[0]
        return int(books_in_cart)

    @allure.step("ui.очистка корзины")
    def clear_cart(self):
        """очищаем корзину"""
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".b-link-popup.basket-header-links")))
        self.__driver.find_element(
            By.XPATH, "//span[@class='b-link-popup basket-header-links'"
            "and normalize-space(text())='Очистить корзину']").click()

    @allure.step("ui.вывод стоимостей товара в корзине")
    def price_check(self):
        """проверяем что стоимость книги равна стоимости при оформлении заказа,
        применяются скидки"""
        items_value = self.__driver.find_element(
            By.CLASS_NAME, "book-price").text
        items_price = items_value.split()[0]
        check_out_value = self.__driver.find_element(
            By.ID, "basket-default-sumprice-discount"
            ).text
        check_out_price = check_out_value.split()[0]
        return int(items_price), int(check_out_price)
