""""Этот файл содержит тесты для проверки API
книжного интернет-магазина Лабиринт"""

import pytest
import allure
from lab_api.LabApi import LabirintApi
from creds import *

api = LabirintApi(base_url)


@allure.epic("Final_project")
@allure.title("Поиск по ID книги")
@allure.id("LAB_6")
@allure.story("API_test")
@allure.feature("API")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_id():
    with allure.step("Поиск по ID {item_id} книги"):
        resp = api.search_book_by_id(item_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.title("Поиск по автору")
@allure.feature("API")
@allure.id("LAB_7")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_author():
    with allure.step("Поиск по ID {author_id} автора"):
        resp = api.search_item_by_author(author_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.id("LAB_8")
@allure.title("Поиск по канцтоварам")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_office_id():
    with allure.step("Поиск по ID {office_id} канцтоваров"):
        resp = api.search_item_from_office(office_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.id("LAB_9")
@allure.title("Поиск по сувенирам")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_souvenir_id():
    with allure.step("Поиск по ID {souvenir_id} сувенира"):
        resp = api.search_item_from_souvenir(souvenir_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск по журналам")
@allure.id("LAB_10")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_journal_id():
    with allure.step("Поиск по ID {journal_id} журнала"):
        resp = api.search_item_from_journals(journal_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск по играм")
@allure.id("LAB_11")
@pytest.mark.api
@pytest.mark.positive_test
def test_search_by_games_id():
    with allure.step("Поиск по ID {game_id} игры"):
        resp = api.search_item_from_games(game_id)
        assert resp.status_code == 200


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск несуществующей книги")
@allure.id("LAB_12")
@pytest.mark.api
@pytest.mark.negative_test
def test_search_by_wrong_id():
    with allure.step("Поиск книги по несуществующему ID {wrong_item_id}"):
        resp = api.search_book_by_id(str(wrong_item_id))
        assert resp.status_code == 404


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск по несуществующему автору")
@allure.id("LAB_13")
@pytest.mark.api
@pytest.mark.negative_test
def test_search_by_wrong_author_id():
    with allure.step("Поиск книги по автору с несуществующим ID {wrong_author_id}"):
        resp = api.search_book_by_id(str(wrong_author_id))
        assert resp.status_code == 404


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск несуществующего раздела")
@allure.id("LAB_14")
@pytest.mark.api
@pytest.mark.negative_test
def test_search_by_wrong_genre_id():
    with allure.step("Поиск по несуществующему разделу {wrong_genre}"):
        resp = api.search_by_genre(str(wrong_genre))
        assert resp.status_code == 404


@allure.epic("Final_project")
@allure.story("API_test")
@allure.feature("API")
@allure.title("Поиск по издательству")
@allure.id("LAB_15")
@pytest.mark.api
@pytest.mark.negative_test
def test_search_by_publishing_house():
    with allure.step("Поиск книги по издательству"):
        resp = api.search_by_publishing_house()
        assert resp.status_code == 404