import random
import sys
import requests
from bs4 import BeautifulSoup
from random import shuffle
from nltk.tokenize import RegexpTokenizer
from config import Settings
import pathlib


dict_words = set()

settings = Settings.from_json(pathlib.Path('./config.json'))

BASE_number_recursion = 2000
BASE_number_articles = settings.BASE_number_articles
BASE_start_URL = settings.BASE_start_URL

sys.setrecursionlimit(BASE_number_recursion)


def check_word(list_of_words: list) -> list:
    """Check is first letter in word russian letter or not.

    Args:
        list_of_words: List where save words that need to check.

    Returns:
        List where words that contains first russian letter were replace on space.
    """
    for index, word in enumerate(list_of_words):
        for character in word:
            if not ((ord(character) >= 1072) and (ord(character) <= 1103)):
                list_of_words[index] = ' '

    return list_of_words


def write_to_file(article_text: str) -> None:
    """Write the text of the article to file.

    Args:
        article_text: The text of the article.

    Returns:
        None.
    """
    count = random.randrange(0, 100000, 1)
    lines = (line.strip() for line in article_text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    try:
        with open(f'data/{count}.txt', 'w', encoding='utf-8') as file:
            for line in text:
                file.write(line)
    except:
        print('not good name')


def remove_digits(response: requests) -> str:
    """Remove digits from the text of the article.

    Args:
        response: Object that contains information that server sent.

    Returns:
        Text of the article without digits.
    """
    soup = BeautifulSoup(response.text, features="html.parser")
    write_to_file(soup.get_text())
    text = soup.get_text().lower()

    return ''.join([i for i in text if not i.isdigit()])


def find_underlining(list_of_elements: list) -> list:
    """Find underlinig in the dictionary.

    Args:
        list_of_elements: The list that contains all words.

    Returns:
        List of words that does not have underlining.
    """
    temp_list = []
    for index, value in enumerate(list_of_elements):
        if value.find('_'):
            temp = value.split('_')
            for item in temp:
                temp_list.append(item)
            list_of_elements[index] = ' '

    for item in temp_list:
        list_of_elements.append(item)

    return list_of_elements


def create_data(response: requests) -> None:
    """Start to parse wikipedia and create data for check_sentence.py

    Args: Object that contains information that server sent.

    Returns:
         None.
    """
    text = remove_digits(response)

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    sort_tokens = check_word(tokens)
    new_tokens = set(sort_tokens)

    temp_value = set(find_underlining(list(new_tokens)))
    new_temp_value = set(check_word(list(temp_value)))
    new_temp_value.remove(' ')

    dict_words.update(new_temp_value)


def create_dictionary(diction: set) -> None:
    """Create dictionary with all words that were parsed from articles.

    Args:
        diction: Set that contains all words that were parsed from articles.

    Returns:
        None.
    """
    with open('data/dictionary.txt', 'w', encoding='utf-8') as file:
        for item in diction:
            file.write(item + '\n')


def find_link_to_parse(all_links: list):
    """Find the correct link that can parse.

    Args:
        all_links: List of links to find correct link.

    Returns:
         Link that can parse.
    """
    link_to_parse = 0
    for link in all_links:
        try:
            if link.get('href').find('/wiki/') == -1:
                continue
            else:
                if link.get('href')[-3:] not in ['svg', 'png', 'jpg', 'bmp'] and link.get('href')[0:4] != 'http' and link.get('href').find('wikimedia') == -1:
                    link_to_parse = link
                    break
        except:
            pass
    return link_to_parse


def start_parse(url: str, counter: int) -> None:
    """Will do preprocessing before start parse wiki page.

    Args:
        url: URL of the web page to make request to this page.
        counter: Counter that count number of article to parse.
    Returns:
        None.
    """
    if counter == 0:
        create_dictionary(dict_words)
        exit()
    print(f'Article: {url}')
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find(id="firstHeading")
    print(f'Article title: {title.text}')
    create_data(response)

    all_links = soup.find(id='bodyContent').find_all('a')
    shuffle(all_links)
    link_to_parse = find_link_to_parse(all_links)

    print(f'Words in dictionary: {len(dict_words)}')
    print('\n\n')
    counter = counter - 1
    if link_to_parse == 0:
        shuffle(all_links)
        new_link = find_link_to_parse(all_links)
        start_parse('https://ru.wikipedia.org' + new_link.get('href'), counter)
    else:
        start_parse('https://ru.wikipedia.org' + link_to_parse.get('href'), counter)


if __name__ == '__main__':
    start_parse(BASE_start_URL, counter=BASE_number_articles)

