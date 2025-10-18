""""Этот файл содержит тесты для проверки API
книжного интернет-магазина Лабиринт"""

import pytest
import allure
from lab_api.LabApi import LabirintApi
from creds import (
    base_url, item_id, author_id, wrong_item_id, wrong_author_id,
    wrong_genre, office_id, souvenir_id, journal_id, game_id)

api = LabirintApi(base_url)


@allure.epic("Final_project")
@allure.id("LABIRINT_1")
@allure.story("API_test")
@allure.feature("API")
def test_search_by_id():
    resp = api.search_book_by_id(item_id)
    assert resp.status_code == 200


@pytest.mark.positive_test
def test_search_by_author():
    resp = api.search_item_by_author(author_id)
    assert resp.status_code == 200


@pytest.mark.positive_test
def test_search_by_office_id():
    resp = api.search_item_from_office(office_id)
    assert resp.status_code == 200


@pytest.mark.positive_test
def test_search_by_souvenir_id():
    resp = api.search_item_from_souvenir(souvenir_id)
    assert resp.status_code == 200


@pytest.mark.positive_test
def test_search_by_journal_id():
    resp = api.search_item_from_journals(journal_id)
    assert resp.status_code == 200

@pytest.mark.positive_test
def test_search_by_games_id():
    resp = api.search_item_from_games(game_id)
    assert resp.status_code == 200

@pytest.mark.negative_test
def test_search_by_wrong_id():
    resp = api.search_book_by_id(str(wrong_item_id))
    assert resp.status_code == 404

@pytest.mark.negative_test
def test_search_by_wrong_author_id():
    resp = api.search_book_by_id(str(wrong_author_id))
    assert resp.status_code == 404


@pytest.mark.negative_test
def test_search_by_wrong_genre_id():
    resp = api.search_by_genre(str(wrong_genre))
    assert resp.status_code == 404


@pytest.mark.negative_test
def test_search_by_publishing_house():
    resp = api.search_by_publishing_house()
    assert resp.status_code == 404