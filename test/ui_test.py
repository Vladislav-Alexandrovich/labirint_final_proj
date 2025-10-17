# import allure
from lab_pages.MainPage import MainPage
from lab_pages.CartPage import CartPage


# def test_books_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_books()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/books/'

# def test_foreignbooks_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_foreignbooks()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/foreignbooks/'


# def test_best_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_best()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/best/'


# def test_school_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_school()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/school/'


# def test_office_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_office()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/office/'

# def test_games_redirect(browser):
#     main_page = MainPage(browser)
#     main_page.put_cookie()
#     main_page.click_on_games()
    
#     assert main_page.get_current_url() == 'https://www.labirint.ru/games/'

# def test_empty_cart(browser):
#     cart_page = CartPage(browser)
#     cart_page.put_cookie()
#     empty_cart_message = cart_page.check_empty_cart()
    
#     assert empty_cart_message == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'

# def test_filled_cart(browser):
#     cart_page = CartPage(browser)
#     cart_page.put_cookie()
#     books_in_cart = cart_page.put_item_in_cart()

#     assert books_in_cart == 1

def test_clear_cart(browser):
    cart_page = CartPage(browser)
    cart_page.put_cookie()
    books_in_cart, empty_cart_message = cart_page.clear_cart()

    assert books_in_cart == 1
    assert empty_cart_message == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'
