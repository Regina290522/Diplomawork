# Diploma-work
1. Склонировать проект в Pycharm: кликнуть вкладку Commit, отметить галочкой Changes, далее выбрать файлы, написать комментарий и нажать Commit and Push и далее нажимаем в открывшемся окне Push
   Для установки зависимостей проекта выполните команду: pip install -r requirements.txt
   Для запуска тестов: pytest
   Для выполнения всех тестов: pytest --alluredir=allure-results
   Для генерации отчетов в формате Allure: allure serve allure-results
   Ссылка на дипломную работу в Github: https://github.com/Regina290522/Diplomawork
2. Получение токена: Чтобы получить токен, необходимо зайти на сайт Читай-город (https://www.chitai-gorod.ru/), через вкладку DevTools, выбираем вкладку Network, далее находим наш запрос в колонке Name, и во вкладке Headers, находим в разделе Request Headers наш Cookie и это значение применяем в token в test_api.py, который мы добавляем в коллекцию в Postmane, для успешного прохождения тестов.
3. Шаги работы: 
Подключение зависимостей: selenium - библиотека для автоматизации UI тестирования;
   requests - библиотека для работы с HTTP-клиентом, используемая для API тестирования;
   pytest - основная библиотека для написания и выполнения тестов;
   allure - библиотека для генерации отчетов о выполнении тестов.
4. Структура: тесты для проекта интернет-магазина книг Читай-город (https://www.chitai-gorod.ru/)
тесты: test_ui.py; test_ui.py
requirements.txt — файл с зависимостями проекта;
README.md — описание проекта и инструкция.