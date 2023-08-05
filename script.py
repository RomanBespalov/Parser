import requests
import sqlite3

from bs4 import BeautifulSoup


def parse_url(url):
    """Функция для парсинга данных по урл."""
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')

        target_tag_1 = soup.find('div', class_='TT9eCd')  # средняя оценка
        target_tag_2 = soup.find('div', class_='g1rdde')  # количество отзывов
        target_tag_3 = soup.find_all(
            'div', class_='ClM7O'
        )  # количество скачиваний

        if target_tag_1:
            text = target_tag_1.get('aria-label')
            reviews_count = text.split()[1]
            a = f"Средняя оценка: {reviews_count}"

        if target_tag_2:
            text = target_tag_2.get_text()
            number = text.split()[0]
            b = f"Количество отзывов: {number}"

        if target_tag_3:
            for tag in target_tag_3:
                if '+' in tag.get_text():
                    c = f"Количество скачиваний: {tag.get_text()}"

        return [a, b, c]

    else:
        print(f"Ошибка при получении страницы. "
              f"Код статуса: {response.status_code}")


db_connection = sqlite3.connect('parse.db')
db_cursor = db_connection.cursor()
db_cursor.execute('''CREATE TABLE IF NOT EXISTS parse (
                        domain TEXT,
                        link TEXT,
                        output TEXT
                     )''')


file_path = "gplay_urls.txt"
with open(file_path, "r") as file:
    lines = file.read().splitlines()

for line in lines[1:]:
    domain, link = line.split('\t')
    data = parse_url(link)
    string_data = ', '.join(data)
    db_cursor.execute(
        'INSERT INTO parse (domain, link, output) '
        'VALUES (?, ?, ?)', (domain, link, string_data)
    )


db_connection.commit()
db_connection.close()
