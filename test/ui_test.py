import allure
import pytest
from creds import (item_to_search, empty_search, base_url)
from lab_pages.MainPage import MainPage
from lab_pages.CartPage import CartPage
from lab_pages.SearchPage import SearchPage


@allure.epic("Final_project")
@allure.id("LABIRINT_1")
@allure.story("UI_test")
@allure.feature("Main_page_ui")
@pytest.mark.ui
@pytest.mark.positive_test
# @pytest.mark.skip(reason='working')
def smoke_test_all_search_headers(browser):
    """Этот тест содержит необходимые проверки для основных товарных вкладок"""
    with allure.step("Передать драйвер"):
        main_page = MainPage(browser)

    # with allure.step("Передать куки"):
    #     main_page.put_cookie()

    with allure.step("Проверка вкладки Книги"):
        books_header = main_page.click_on_books()
        assert main_page.get_current_url() == (base_url + "books/")
        assert main_page.get_current_url() != base_url
        assert books_header == 'Книги'

    with allure.step("Проверка вкладки Иностранные издания"):
        foreing_headers = main_page.click_on_foreignbooks()
        assert main_page.get_current_url() == (base_url + "foreignbooks/")
        assert main_page.get_current_url() != base_url
        assert foreing_headers == 'Книги на иностранном языке'

    with allure.step("Проверка вкладки Главное"):
        best_header = main_page.click_on_best()
        assert main_page.get_current_url() == (base_url + "best/")
        assert main_page.get_current_url() != base_url
        assert best_header == 'Главные книги 2025'

    with allure.step("Проверка вкладки Школа"):
        school_header = main_page.click_on_school()
        assert main_page.get_current_url() == (base_url + "school/")
        assert main_page.get_current_url() != base_url
        assert school_header == 'Все учебники в Лабиринте'

    with allure.step("Проверка вкладки Канцтовары"):
        office_header = main_page.click_on_office()
        assert main_page.get_current_url() == (base_url + "office/")
        assert main_page.get_current_url() != base_url
        assert office_header == "Канцелярские товары"

    with allure.step("Проверка вкладки Игрушки"):
        games_header = main_page.click_on_games()
        assert main_page.get_current_url() == (base_url + "games/")
        assert main_page.get_current_url() != base_url
        assert games_header == "Игры и игрушки"

    with allure.step("Проверка вкладки Еще"):
        multimedia_header = main_page.more_multimedia()
        assert main_page.get_current_url() != base_url
        souvenir_header = main_page.more_souvenir()
        assert main_page.get_current_url() != base_url
        journals_header = main_page.more_journals()
        assert main_page.get_current_url() != base_url
        assert multimedia_header == 'Мультимедиа'
        assert souvenir_header == 'Сувениры'
        assert journals_header == 'Журнальный лабиринт'


@allure.feature("Cart_page_ui")
@pytest.mark.ui
@pytest.mark.positive_test
# @pytest.mark.skip(reason='working')
def smoke_test_cart_functions(browser):
    """Этот тест содержит необходимые проверки работы корзины"""
    with allure.step("Передать драйвер"):
        cart_page = CartPage(browser)

    # with allure.step("Передать куки"):
    #     cart_page.put_cookie()

    with allure.step("Проверка пустой корзины"):
        empty_cart_message = cart_page.check_empty_cart()
        assert empty_cart_message == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'
    
    with allure.step("Наполнение корзины"):
        books_in_cart = cart_page.put_item_in_cart()
        assert books_in_cart == 1

    with allure.step("Очистка корзины"):
        cart_page.clear_cart()

    with allure.step("Проверка очищенной корзины"):
        empty_cart_message = cart_page.check_empty_cart()
        assert empty_cart_message == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'


@pytest.mark.ui
@pytest.mark.positive_test
# @pytest.mark.skip(reason='working')
def price_test(browser):
    """Этот тест содержит проверку стоимости товара в корзине
    со стоимостью при оформлении заказа"""
    with allure.step("Передать драйвер"):
        cart_page = CartPage(browser)

    # with allure.step("Передать куки"):
    #     cart_page.put_cookie()

    with allure.step("Проверка пустой корзины"):
        empty_cart_message = cart_page.check_empty_cart()
        assert empty_cart_message == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'

    with allure.step("Наполнение корзины"):
        books_in_cart = cart_page.put_item_in_cart()
        assert books_in_cart == 1

    with allure.step("Проверка стоимости книги"):
        items_price, check_out_price = cart_page.price_check()
        assert items_price == check_out_price


@allure.feature("Search_page_ui")
@pytest.mark.ui
@pytest.mark.positive_test
# @pytest.mark.skip(reason='working')
def test_search_book(browser):
    """Этот тест проверяет что поиск выдает результаты"""
    with allure.step("Передать драйвер"):
        main_page = MainPage(browser)
        search_page = SearchPage(browser)
    # with allure.step("Передать куки"):
    #     main_page.put_cookie()
    with allure.step("Передать значение {item_to_search} для поиска"):
        main_page.search(item_to_search)
    with allure.step("Посчитать количество товаров на странице"):
        number_of_goods = search_page.goods_counter()
    with allure.step("Проверить что товары действительно выдаются поиском"):
        assert number_of_goods > 0


@pytest.mark.ui
@pytest.mark.negative_test
# @pytest.mark.skip(reason='working')
def test_empty_search(browser):
    """Этот тест проверяет что пустой поиск не выдает результатов"""
    with allure.step("Передать драйвер"):
        main_page = MainPage(browser)
        search_page = SearchPage(browser)
    # with allure.step("Передать куки"):
    #     main_page.put_cookie()
    with allure.step("Передать значение {empty_search} для поиска"):
        main_page.search(empty_search)
    with allure.step("Посчитать количество товаров на странице"):
        number_of_goods = search_page.goods_counter()
    with allure.step("Проверить что поиск не выдал товаров"):
        assert number_of_goods == 0