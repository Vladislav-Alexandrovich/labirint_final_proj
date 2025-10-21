import random

base_url: str = "https://www.labirint.ru/"
item_to_search: str = "Азбука"
empty_search: str = " "
item_id = "849905"
right_title = "Книга: \
Букварь - Александра Воскресенская. \
Купить книгу, читать рецензии | Лабиринт"
author_id = "207351"
right_author_title = "Автор: Воскресенская Александра Ильинична \
| новинки 2025 \
| книжный интернет-магазин Лабиринт"
office_id = "952347"
right_office_title = "Книга: Закладка № 05 Цветочная - \
. Купить книгу, читать рецензии | Лабиринт"
souvenir_id = "933128"
right_souvenir_title = "Книга: Пакет подарочный, малый - \
. Купить книгу, читать рецензии | Лабиринт"
game_id = "795657"
right_game_title = 'Книга: Алмазные узоры "Пуанты", \
30х30 см - . Купить книгу, читать рецензии | Лабиринт'
journal_id = "diletant-february"
right_journal_title = "«Дилетант» в феврале"

wrong_item_id = random.randint(1000000, 10000000)
wrong_author_id = random.randint(1000000, 10000000)
wrong_genre = random.randint(1000000, 10000000)
