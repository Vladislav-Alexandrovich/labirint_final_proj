import random

base_url: str = "https://www.labirint.ru/"
item_to_search: str = "Азбука"
empty_search: str = " "
item_id: str = "849905"
right_title: str = "Книга: \
Букварь - Александра Воскресенская. \
Купить книгу, читать рецензии | Лабиринт"
author_id: str = "207351"
right_author_title: str = "Автор: Воскресенская Александра Ильинична \
| новинки 2025 \
| книжный интернет-магазин Лабиринт"
office_id: str = "952347"
right_office_title: str = "Книга: Закладка № 05 Цветочная - \
. Купить книгу, читать рецензии | Лабиринт"
souvenir_id: str = "933128"
right_souvenir_title: str = "Книга: Пакет подарочный, малый - \
. Купить книгу, читать рецензии | Лабиринт"
game_id: str = "795657"
right_game_title: str = 'Книга: Алмазные узоры "Пуанты", \
30х30 см - . Купить книгу, читать рецензии | Лабиринт'
journal_id: str = "diletant-february"
right_journal_title: str = "«Дилетант» в феврале"

wrong_item_id: str = str(random.randint(1000000, 10000000))
wrong_author_id: str = str(random.randint(1000000, 10000000))
wrong_genre: str = str(random.randint(1000000, 10000000))
