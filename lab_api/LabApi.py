""""Этот файл содержит запросы для проверки API
книжного интернет-магазина Лабиринт"""

from bs4 import BeautifulSoup
import allure
import requests


class LabirintApi:
    def __init__(self, base_url):
        self.url = base_url

    @allure.step("api. поиск по id {product_id} книги")
    def search_book_by_id(self, product_id):
        resp = requests.get(self.url + 'books/' + product_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        book_title = soup.title.string
        return resp, book_title

    @allure.step("api. поиск по id {office_id} канцтоваров")
    def search_item_from_office(self, office_id):
        resp = requests.get(self.url + 'office/' + office_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        office_title = soup.title.string
        return resp, office_title

    @allure.step("api. поиск по id {souvenir_id} сувениров")
    def search_item_from_souvenir(self, souvenir_id):
        resp = requests.get(self.url + 'souvenir/' + souvenir_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        souvenir_title = soup.title.string
        return resp, souvenir_title

    @allure.step("api. поиск по id {journal_id} журналов")
    def search_item_from_journals(self, journal_id):
        resp = requests.get(self.url + 'journals/' + journal_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        journal_title = soup.title.string
        return resp, journal_title

    @allure.step("api. поиск по id {game_id} игр")
    def search_item_from_games(self, game_id):
        resp = requests.get(self.url + 'games/' + game_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        game_title = soup.title.string
        return resp, game_title

    @allure.step("api. поиск по id {author_id} автора")
    def search_item_by_author(self, author_id):
        resp = requests.get(self.url + 'authors/' + author_id)
        soup = BeautifulSoup(resp.content, 'html.parser')
        author_title = soup.title.string
        return resp, author_title

    @allure.step("api. поиск по жанру {genre_id}")
    def search_by_genre(self, genre_id):
        resp = requests.get(self.url + 'genre/' + genre_id)
        return resp

    @allure.step("api. поиск по издательству")
    def search_by_publishing_house(self):
        resp = requests.get(self.url + "pubhouse/" + "books")
        return resp
