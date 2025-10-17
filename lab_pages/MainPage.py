import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        """открываем страницу"""
        # self.__url = "https://www.labirint.ru/"
        # self.__driver = driver
        self.__driver = driver
        self.__driver.get("https://www.labirint.ru/")
        
    def put_cookie(self):
        """передаем куки"""
        cookie = {'name': 'cookie_policy', 'value': '1'}
        self.__driver.add_cookie(cookie)
        self.__driver.refresh()

    def click_on_books(self):
        """кликаем на вкладку Книги"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        books_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return str(books_header)
    
    def click_on_foreignbooks(self) -> str:
        """кликаем на вкладку Иностранные издания"""
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/foreignbooks/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/foreignbooks/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        foreign_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return str(foreign_header)
    
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
    
    # def click_on_school(self) -> str:
    #     """кликаем на вкладку Школа"""
    #     WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/school/' and @class='b-header-b-menu-e-text']")))
    #     self.__driver.find_element(By.CSS_SELECTOR, "a[href='/school/']").click()
    #     # self.__driver.find_element(By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/school/"]').click()
    #     WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.school-cap__header')))
    #     school_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.school-cap__header').text
    #     return school_header
    
    def click_on_school(self) -> str:
        """переходим на страницу Школа"""
        self.__driver.get("https://www.labirint.ru/school/")
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.school-cap__header')))
        school_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.school-cap__header').text
        return school_header

    def click_on_office(self) -> str:
      
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
        office_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return office_header
    
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
        game_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return game_header
    
    def more_multimedia(self) -> str:
        """переходим в раздел Мультимедиа"""
        self.__driver.get("https://www.labirint.ru/multimedia/")
        multimedia_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return multimedia_header
    
    def more_souvenir(self) -> str:
        """переходим в раздел Сувениры"""
        self.__driver.get("https://www.labirint.ru/souvenir/")
        souvenir_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1.genre-name').text
        return souvenir_header
    
    def more_journals(self) -> str:
        """переходим в раздел Журналы"""
        self.__driver.get("https://www.labirint.ru/journals/")
        journals_header = self.__driver.find_element(By.CSS_SELECTOR, 'h1').text
        return journals_header

    def get_current_url(self) -> str:
        """получаем адрес текущей страницы"""
        current_url = self.__driver.current_url
        return current_url
