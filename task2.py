# В нашей школе мы не можем разглашать персональные данные пользователей,
# Но чтобы преподаватель и ученик смогли объяснить нашей поддержке,
# Кого они имеют в виду (у преподавателей, например, часто учится несколько Саш),
# Мы генерируем пользователям уникальные и легко произносимые имена.
#
# Имя у нас состоит из прилагательного, имени животного и двузначной цифры.
# В итоге получается, например, "Перламутровый лосось 77".
#
# Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных (https://inlnk.ru/jElywR)
# И вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
#
# А: 642
# Б: 412
# В:....


import requests
from bs4 import BeautifulSoup


class WikiParser:
    url_prefix = r'https://ru.wikipedia.org'
    dictionary = {letter: 0 for letter in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'}

    def __init__(self):
        self.page = requests.get(r'https://inlnk.ru/jElywR')
        self.bs = BeautifulSoup(self.page.text, 'html.parser')

    def get_new_url(self):
        block = self.bs.find('div', id='mw-pages')
        urls = block.find_all('a', href=True)
        for url in urls:
            if url.text == 'Следующая страница':
                self.page = requests.get(self.url_prefix + url['href'])
                self.bs = BeautifulSoup(self.page.text, 'html.parser')
                return True
        return False

    def parse(self):
        list_part = self.bs.find('div', class_='mw-category mw-category-columns')
        blocks = list_part.find_all('div', class_='mw-category-group')
        for block in blocks:
            letter = block.find('h3').text
            animals = block.find_all_next('li')
            if letter in self.dictionary:
                self.dictionary[letter] += len(animals)
            else:
                return False
        return True

    def __str__(self):
        result = ''
        for key, value in self.dictionary.items():
            result += f'{key}: {value}\n'
        return result


def task():
    parser = WikiParser()
    while True:
        if parser.parse() and parser.get_new_url():
            continue
        break
    print(parser)


if __name__ == '__main__':
    task()
