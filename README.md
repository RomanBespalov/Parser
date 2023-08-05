# Парсер данных

Этот проект представляет собой скрипт для парсинга данных с указанных URL-адресов и сохранения результатов в базу данных SQLite.

## Установка и запуск
1. Склонируйте репозиторий себе на компьютер: git clone git@github.com:RomanBespalov/parsing.git
2. Перейдите в директорию проекта (parsing) и создайте виртуальное окружение: python3 -m venv venv
3. Активируйте виртаульное окружение: source venv/bin/activate
4. Установите зависимости из файла requirements.txt: pip install -r requirements.txt
5. Запустите файл со скриптом: python3 script.py
6. После успешного выполнения скрипта, в директории будет создана БД со всеми данными - parse.db

### Использование
Скрипт script.py читает URL-адреса из файла gplay_urls.txt, выполняет парсинг данных с указанных страниц Google Play и сохраняет результаты в базу данных parse.db. Файл test_task.pdf содержит ТЗ к проекту.

### Входные данные:

Файл gplay_urls.txt: текстовый файл, содержащий список доменов и ссылок на страницы Google Play.

### Выходные данные:

База данных parse.db: SQLite база данных, содержащая результаты парсинга данных.
