import allure
import pytest
from lab_pages.MainPage import MainPage
from lab_pages.CartPage import CartPage


@allure.epic("Final_project")
@allure.id("LABIRINT_1")
@allure.story("UI_test")
@allure.feature("Main_page_ui")
@pytest.mark.ui
def smoke_test_all_search_headers(browser):
    """Этот тест содержит необходимые проверки для основных товарных вкладок"""
    with allure.step("Передать драйвер"):
        main_page = MainPage(browser)

    with allure.step("Передать куки"):
        main_page.put_cookie()

    with allure.step("Проверка вкладки Книги"):
        books_header = main_page.click_on_books()
        assert main_page.get_current_url() == 'https://www.labirint.ru/books/'
        assert books_header == 'Книги'

    with allure.step("Проверка вкладки Иностранные издания"):
        foreing_headers = main_page.click_on_foreignbooks()
        assert main_page.get_current_url() == 'https://www.labirint.ru/foreignbooks/'
        assert foreing_headers == 'Книги на иностранном языке'

    with allure.step("Проверка вкладки Главное"):
        best_header = main_page.click_on_best()
        assert main_page.get_current_url() == 'https://www.labirint.ru/best/'
        assert best_header == 'Главные книги 2025'

    with allure.step("Проверка вкладки Школа"):
        school_header = main_page.click_on_school()
        assert main_page.get_current_url() == 'https://www.labirint.ru/school/'
        assert school_header == 'Все учебники в Лабиринте'

    with allure.step("Проверка вкладки Канцтовары"):
        office_header = main_page.click_on_office()
        assert main_page.get_current_url() == 'https://www.labirint.ru/office/'
        assert office_header == "Канцелярские товары"

    with allure.step("Проверка вкладки Игрушки"):
        games_header = main_page.click_on_games()
        assert main_page.get_current_url() == 'https://www.labirint.ru/games/'
        assert games_header == "Игры и игрушки"

    with allure.step("Проверка вкладки Еще"):
        multimedia_header = main_page.more_multimedia()
        souvenir_header = main_page.more_souvenir()
        journals_header = main_page.more_journals()
        assert multimedia_header == 'Мультимедиа'
        assert souvenir_header == 'Сувениры'
        assert journals_header == 'Журнальный лабиринт'


@allure.feature("Main_page_ui")
@pytest.mark.ui
def smoke_test_cart_functions(browser):
    """Этот тест содержит необходимые проверки работы корзины"""
    with allure.step("Передать драйвер"):
        cart_page = CartPage(browser)

    with allure.step("Передать куки"):
        cart_page.put_cookie()

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