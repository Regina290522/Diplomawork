import allure
import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOiJjMzBiNTVkN2MxMWQ1ODgxMDg2ZDUyYjE1YWI1MGRlOWZlMTU1ZjMyNDNiMzVhN2Q2NGVkMjU3NDJmZGRkNDQ4IiwiaWF0IjoxNzMzOTAxNTIyLCJleHAiOjE3MzM5MDUxMjIsInR5cGUiOjEwfQ.0GbzfJ9yDDgMlKBki3IxQkeOt-AUn1n0XTw7KWegVgA'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


@allure.title("Проверка запроса нахождение книги")
@allure.description("Проверка отправки get запроса для получения информации о книге")
@allure.severity("Critical")
def test_get_book():
    url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=война и мир'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'data' in response.json()


@allure.title("Проверка запроса нахождение книги c другим названием")
@allure.description("Проверка отправки get запроса для получения информации о книге")
@allure.severity("Critical")
def test_get_book_name():
    url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=преступление и наказание'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'data' in response.json()


@allure.title("Неверный данные для поиска")
@allure.description("Проверка  запроса с неверным методом")
@allure.severity("Critical")
def test_get_book_pusto():
        url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase='
        response = requests.get(url, headers=headers)

        assert response.status_code == 200


@allure.title("Неверный метод")
@allure.description("Проверка  запроса с неверным методом")
@allure.severity("Critical")
def test_get_book_negative_post():
    url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=война и мир'
    response = requests.post(url, headers=headers)

    assert response.status_code == 405

@allure.title("Неверный данные для поиска")
@allure.description("Проверка  запроса с неверным методом")
@allure.severity("Critical")
def test_get_book_negative_simbol():
    url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase=$%$@#@^'
    response = requests.get(url, headers=headers)

    assert response.status_code == 401

