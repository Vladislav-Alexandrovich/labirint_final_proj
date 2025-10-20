import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import base_url


class MainPage:
    """В этом классе хранятся методы для открытия вкладок
и работы с главной страницей"""
    @allure.step("ui.открытие браузера")
    def __init__(self, driver: WebDriver) -> None:
        """открываем страницу"""
        self.__driver = driver

    @allure.step("ui.клик на вкладку Книги")
    def click_on_books(self) -> str:
        """кликаем на вкладку Книги"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        books_header = self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.genre-name').text
        return str(books_header)

    @allure.step("ui.клик на вкладку Иностранные издания")
    def click_on_foreignbooks(self) -> str:
        """кликаем на вкладку Иностранные издания"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '.b-header-b-menu-e-text[href="/'
                                        'foreignbooks/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR,
            '.b-header-b-menu-e-text[href="/foreignbooks/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        foreign_header = self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.genre-name').text
        return str(foreign_header)

    @allure.step("ui.клик на вкладку Главное")
    def click_on_best(self) -> str:
        """кликаем на вкладку Главное"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/best/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/best/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h1[text()='Главные книги 2025']")))
        # By.CSS_SELECTOR, "h1:contains('Главные книги 2025')"
        best_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1').text
        return str(best_header)

    @allure.step("ui.клик на вкладку Школа")
    def click_on_school(self) -> str:
        """кликаем на вкладку Школа"""
        school_element = self.__driver.find_elements(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/school/"]')
        school_element[1].click()
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.school-cap__header')))
        school_header = self.__driver.find_element(
            By.CSS_SELECTOR, 'h1.school-cap__header').text
        return school_header

    # @allure.step("ui.переход в раздел Школа")
    # def click_on_school(self) -> str:
    #     """переходим на страницу Школа"""
    #     self.__driver.get(base_url + "school/")
    #     # WebDriverWait(self.__driver, 10).until(
    #     #     EC.visibility_of_element_located((By.CSS_SELECTOR,
    #     #                                       'h1.school-cap__header')))
    #     school_header = self.__driver.find_element(
    #         By.CSS_SELECTOR,
    #         'h1.school-cap__header').text
    #     return school_header

    @allure.step("ui.клик на вкладку Канцтовары")
    def click_on_office(self) -> str:
        """кликаем на вкладку Канцтовары"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]'
            ).click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        office_header = self.__driver.find_element(By.CSS_SELECTOR,
                                                   'h1.genre-name').text
        return office_header

    @allure.step("ui.клик на вкладку Игрушки")
    def click_on_games(self) -> str:
        """кликаем на вкладку Игрушки"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/games/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/games/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        game_header = self.__driver.find_element(By.CSS_SELECTOR,
                                                 'h1.genre-name').text
        return game_header

    @allure.step("ui.переход в раздел Мультимедиа")
    def more_multimedia(self) -> str:
        """переходим в раздел Мультимедиа"""
        self.__driver.get(base_url + "multimedia/")
        multimedia_header = self.__driver.find_element(By.CSS_SELECTOR,
                                                       'h1.genre-name').text
        return multimedia_header

    @allure.step("ui.переход в раздел Сувениры")
    def more_souvenir(self) -> str:
        """переходим в раздел Сувениры"""
        self.__driver.get(base_url + "souvenir/")
        souvenir_header = self.__driver.find_element(By.CSS_SELECTOR,
                                                     'h1.genre-name').text
        return souvenir_header

    @allure.step("ui.переход в раздел Журналы")
    def more_journals(self) -> str:
        """переходим в раздел Журналы"""
        self.__driver.get(base_url + "journals/")
        journals_header = self.__driver.find_element(
            By.CSS_SELECTOR, 'h1').text
        return journals_header

    @allure.step("ui.поиск")
    def search(self, term) -> None:
        self.__driver.find_element(By.ID, "search-field").send_keys(term)
        self.__driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("ui.получение адреса текущей страницы")
    def get_current_url(self) -> str:
        """получаем адрес текущей страницы"""
        current_url = self.__driver.current_url
        return current_url
