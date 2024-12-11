import allure
import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQwNzQwNzUsImlhdCI6MTczMzkwNjA3NSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjY1NzNjNWMxMzZhYWM0M2JkM2Q1YTlkMDI4YzIyN2EzN2JlOTQxMDYwOTdjYzlhOGY5YzIzOTkzNjI3NzJjYzEiLCJ0eXBlIjoxMH0.u-qqhJ3mxRTc_MnN-re3cszhAu94lgMLivVuidvuZQ0'
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


@allure.title("Ввод пустых данных для поиска")
@allure.description("Проверка  запроса с пустыми данными")
@allure.severity("Critical")
def test_get_book_pusto():
        url = 'https://web-gate.chitai-gorod.ru/api/v1/recommend/semantic?phrase='
        response = requests.get(url, headers=headers)

        assert response.status_code == 403


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

    assert response.status_code == 200

