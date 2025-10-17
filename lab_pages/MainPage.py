import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        # self.__url = "https://www.labirint.ru/"
        # self.__driver = driver
        self.__driver = driver
        self.__driver.get("https://www.labirint.ru/")
        
    def put_cookie(self):
        cookie = {'name': 'cookie_policy', 'value': '1'}
        self.__driver.add_cookie(cookie)
        self.__driver.refresh()

    def click_on_books(self):

        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/books/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))

    def click_on_foreignbooks(self):
       
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/foreignbooks/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/foreignbooks/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
    
    def click_on_best(self):
       
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/best/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/best/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h1[text()='Главные книги 2025']")))
        # By.CSS_SELECTOR, "h1:contains('Главные книги 2025')"
    
    def click_on_school(self):

        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/schоol/"]')))

        school_button = self.__driver.find_element(By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/school/"]')
        self.__driver.execute_script("arguments[0].click();", school_button)

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.school-cap__header')))

    def click_on_office(self):
      
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/office/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
    
    def click_on_games(self):
      
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/games/"]')))

        self.__driver.find_element(
            By.CSS_SELECTOR, '.b-header-b-menu-e-text[href="/games/"]').click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'h1.genre-name')))
    
    def get_current_url(self):
        current_url = self.__driver.current_url
        return current_url
