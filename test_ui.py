import allure
import pytest
from selenium import webdriver
from Diplomawork.pages.MainPage import MainPage




@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        text = main_page.rus_search('Капитанская дочка')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:52] == "Показываем результаты по запросу «капитанская дочка»"


@allure.title("Пустой поиск")
@allure.description("Тест проверяет вылонение пустого поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_empty_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
         browser = webdriver.Chrome()
         main_page = MainPage(browser)
         main_page.empty_search("")
    with allure.step("Отсутствие действия на сайте"):
         url = browser.current_url
    assert url == "https://www.chitai-gorod.ru/"

@allure.title("Поиск по двум книгам")
@allure.description("Тест проверяет корректное выполнение поиска сразу по нескольким книгам")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        text = main_page.books_search('Бесприданница, Золушка')
    with allure.step("Проверка текста с результатами поиска на странице "):
        assert text[0:56] == "Показываем результаты по запросу «бесприданница золушка»"

@allure.title("Поиск по категории")
@allure.description("Тест проверяет корректное выполнение поиска по категории книг")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        text = main_page.series_search('Книги для детей')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:50] == "Показываем результаты по запросу «книги для детей»"

@allure.title("Просмотр акций")
@allure.description("Тест проверяет открытие страницы с промоакциями")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_promo():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser)
        text = main_page.promotions()
    with allure.step("Проверка текста с результатами поиска на странице"):
         url = browser.current_url
         assert url == "https://www.chitai-gorod.ru/promotions"

         @allure.title("Поиск по каталогу")
         @allure.description("Тест проверяет корректное выполнение поиска, используя каталог")
         @allure.feature("READ")
         @allure.severity("normal")
         @pytest.mark.positive_test
         def test_catalog_search():
             with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
                 browser = webdriver.Chrome()
                 main_page = MainPage(browser)
                 text = main_page.catalog_search()
             with allure.step("Проверка текста в выбранной категории каталога"):
                 assert text[0:14] == "СТИХИ И ПОЭЗИЯ"
