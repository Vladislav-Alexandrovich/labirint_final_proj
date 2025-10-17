import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__driver.get("https://www.labirint.ru/")
        
    def put_cookie(self):
        cookie = {'name': 'cookie_policy', 'value': '1'}
        self.__driver.add_cookie(cookie)
        self.__driver.refresh()

    def check_empty_cart(self):
        self.__driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link[href="/cart/"]').click()   
        empty_cart_message = self.__driver.find_element(By.XPATH, "//span[contains(text(), 'Ваша корзина пуста')]").text
        return empty_cart_message

    def put_item_in_cart(self):
        self.__driver.find_element(By.XPATH, '(//*[@data-carttext])[1]').click()
        self.__driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link[href="/cart/"]').click()
        cart_result = self.__driver.find_element(By.ID, 'basket-default-prod-count2').text
        books_in_cart = cart_result.split()[0]
        return int(books_in_cart)

    def clear_cart(self):
        self.__driver.find_element(By.XPATH, '(//*[@data-carttext])[1]').click()
        self.__driver.find_element(By.CSS_SELECTOR, '.b-header-b-personal-e-link[href="/cart/"]').click()
        cart_result = self.__driver.find_element(By.ID, 'basket-default-prod-count2').text
        books_in_cart = cart_result.split()[0]

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".b-link-popup.basket-header-links")))
        self.__driver.find_element(By.XPATH, "//span[@class='b-link-popup basket-header-links' and normalize-space(text())='Очистить корзину']").click()
        empty_cart_message = self.__driver.find_element(By.XPATH, "//span[contains(text(), 'Ваша корзина пуста')]").text

        return int(books_in_cart), empty_cart_message