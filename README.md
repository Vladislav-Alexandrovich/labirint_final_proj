# labirint_final_proj

## Финальный проект - тестирование веб-приложения книжного интернет магазина Лабиринт

### Шаги
1. Склонировать репозиторий проекта 'git clone https://github.com/Vladislav-Alexandrovich/labirint_final_proj.git'
2. Установить все зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test - тесты
- ./lab_pages - описание страниц
- ./lab_api - апи клиенты

### Команды
#### pytest - запускает все тесты
#### pytest -m ui - запускает тесты пользовательского интерфейса
#### pytest -m api - запускает тесты программного интерфейса
#### pytest --alluredir allure-result - запуск всех тестов с allure
#### pytest  -m ui --alluredir allure-result - запускает тесты пользовательского интерфейса c результатами allure
#### pytest  -m api --alluredir allure-result - запускает тесты программного интерфейса c результатами allure
#### allure serve allure-result - визуализация отчета allure

### Полезные ссылки
- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Ручная часть финальной работы](https://lovenewthings.yonote.ru/share/921183b0-53d8-4ffd-9c6f-da0df6a42d45)

### Библиотеки

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests



