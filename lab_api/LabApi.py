""""Этот файл содержит запросы для проверки API
книжного интернет-магазина Лабиринт"""

import allure
import requests


class LabirintApi:
    def __init__(self, base_url):
        self.url = base_url

    @allure.step("api. поиск по id {product_id} книги")
    def search_book_by_id(self, product_id):
        resp = requests.get(self.url + 'books/' + product_id)
        return resp

    @allure.step("api. поиск по id {office_id} канцтоваров")
    def search_item_from_office(self, office_id):
        resp = requests.get(self.url + 'office/' + office_id)
        return resp

    @allure.step("api. поиск по id {souvenir_id} сувениров")
    def search_item_from_souvenir(self, souvenir_id):
        resp = requests.get(self.url + 'souvenir/' + souvenir_id)
        return resp

    @allure.step("api. поиск по id {journal_id} журналов")
    def search_item_from_journals(self, journal_id):
        resp = requests.get(self.url + 'journals/' + journal_id)
        return resp

    @allure.step("api. поиск по id {game_id} игр")
    def search_item_from_games(self, game_id):
        resp = requests.get(self.url + 'games/' + game_id)
        return resp

    @allure.step("api. поиск по id {author_id} автора")
    def search_item_by_author(self, author_id):
        resp = requests.get(self.url + 'authors/' + author_id)
        return resp

    @allure.step("api. поиск по жанру {genre_id}")
    def search_by_genre(self, genre_id):
        resp = requests.get(self.url + 'genre/' + genre_id)
        return resp

    @allure.step("api. поиск по издательству")
    def search_by_publishing_house(self):
        resp = requests.get(self.url + "pubhouse/" + "books")
        return resp
