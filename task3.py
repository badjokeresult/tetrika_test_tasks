import requests
from bs4 import BeautifulSoup


def get_new_url(bs: BeautifulSoup):
    main_part = bs.find('div', id='mw-pages')
    possible_urls = main_part.find_all('a', href=True)
    for url in possible_urls:
        if url.text == 'Следующая страница':
            return url['href']
    raise Exception()


def parse(dct: dict, url: str):
    page = requests.get(url)
    bs = BeautifulSoup(page.text, 'html.parser')

    parts = bs.find_all('div', class_='mw-category-group')
    for part in parts:
        possible_letters = part.find_all_next('h3')
        letter = None
        for let in possible_letters:
            if len(let.text) == 1:
                letter = let.text
                break
        dct[letter] += len(part.find_all_next('li'))

    return bs


def task():
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    dct = {let: 0 for let in alphabet}
    url_prefix = r'https://ru.wikipedia.org'

    bs = parse(dct, r'https://inlnk.ru/jElywR')
    while True:
        try:
            url = get_new_url(bs)
            bs = parse(dct, url_prefix + url)
        except:
            break

    return dct


if __name__ == '__main__':
    result = task()
    for key in result:
        print(f'{key}: {result[key]}')