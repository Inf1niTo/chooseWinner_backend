# Lottery Backend (Flask)

## Описание

Этот проект представляет собой бэкенд для приложения лотереи,  написанный на Python с использованием фреймворка Flask.  Он предоставляет API для:

- Загрузки списка участников из CSV-файла. (файл должен иметь один столбец, чтение идет со второй строки, тк первая строка - название столбца)
- Расчета победителей на основе курса валюты и выбранного количества победителей.
- Получения списка победителей.
- Генерации Excel-отчета с информацией о розыгрыше.

## Технологии

- Python 3.7+
- Flask
- PyMongo
- pandas
- lxml
- openpyxl
- Flask-CORS

## Установка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Inf1niTo/chooseWinner_backend.git
    ```
2.  **Создайте виртуальное окружение:**
    ```bash
    python -m venv venv
    ```
3.  **Активируйте виртуальное окружение:**
    ```bash
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```
4.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Настройте MongoDB:**
    -  Установите и запустите MongoDB. 
    -  Создайте базу данных  `lottery_db`. (Создатся сама, при запуске кода)

## Запуск

1.  **Запустите Flask-сервер:**
    ```bash
    flask run
    ```
2.  Сервер будет доступен по адресу  `http://127.0.0.1:5000/`. 

## API

-  `/api/upload`  (POST):  Загружает CSV-файл с участниками.
-  `/api/calculate_winners`  (POST):  Рассчитывает победителей.
-  `/api/winners/<int:draw_number>`  (GET):  Получает список новых победителей для розыгрыша.
-  `/api/winners/all/<int:draw_number>`  (GET):  Получает список всех победителей для розыгрыша.
-  `/api/generate_report`  (POST):  Генерирует Excel-отчет.

## Развертывание

Для развертывания приложения на production-сервере:

1.  **Используйте WSGI-сервер,  такой как Gunicorn или uWSGI.**
2.  **Настройте  production-окружение для MongoDB.**
3.  **Настройте обратный прокси-сервер (например,  Nginx)  для перенаправления запросов на ваше Flask-приложение.**

## Дополнительная информация

-  [Документация Flask](https://flask.palletsprojects.com/en/2.3.x/)
-  [Документация PyMongo](https://pymongo.readthedocs.io/en/stable/)
