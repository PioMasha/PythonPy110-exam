import json
import random
from faker import Faker
from conf import MODEL

fake = Faker()


def get_title() -> str:
    """
    Функция генерирует рандомное название произведения
    :return: название в виде строки
    """
    with open("books.txt", "r", encoding="utf-8") as file:
        book_list = file.read().splitlines()
    return random.choice(book_list)


def get_year() -> int:
    """
    Функция генерирует рандомный год издания книги
    :return: год в виде целого числа
    """
    return random.randint(1825, 2010)


def get_pages() -> int:
    """
    Функция генерирует рандомное кол-во страниц книги
    :return: кол-во страниц в виде целого числа
    """
    return random.randint(200, 1100)


def get_isbn13() -> str:
    """
    Функция генерирует фейковый международный станд. книжный номер
    :return: международный станд. книжный номер в виде строки
    """
    return fake.isbn13()


def get_rating() -> float:
    """
    Функция генерирует рандомный рейтинг
    :return: рейтинг в виде десятичного числа
    """
    return round(random.uniform(0, 5), 2)


def get_price() -> float:
    """
    Функция генерирует рандомную цену
    :return: цена в виде десятичного числа
    """
    return round(random.uniform(300, 1500), 1)


def get_author() -> list[str]:
    """
    Функция генерирует фейкового автора
    :return: автор в виде строкового списка
    """
    return [fake.name() for _ in range(random.randint(1, 3))]


def get_book() -> dict:
    """
    Функция генерирует словарь с информацией о книге
    :return: словарь с заполненными данными из пред. функций
    """
    pk = 1
    while True:
        book = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": get_title(),
                "year": get_year(),
                "pages": get_pages(),
                "isbn13": get_isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_author()
            }
        }
        yield book
        pk += 1


def get_books(count_books: int, pk_start: int = 1) -> list[dict]:
    """
    Функция генерирует список книг из словарей
    :param count_books: кол-во книг при генерации - целое число
    :param pk_start: целое число, определяющее начало отсчета
    :return: список книг в виде словаря
    """
    book_generator = get_book()
    books = []
    for _ in range(count_books):
        book = next(book_generator)
        book["pk"] = pk_start
        books.append(book)
        pk_start += 1
    return books


def write_to_json(books: list[dict], filename: str):
    """
    Функция переписывает данные в фор-те JSON
    :param books: список книг в виде словаря
    :param filename: строковое имя файла для записи
    :return: None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4, ensure_ascii=False)


def main():
    """
    Функция формирует список книг из словарей и записывает его в JSON
    :return: возвращает текст
    """
    count_books = 100
    books = get_books(count_books)
    write_to_json(books, "library_books.json")
    return f"{count_books} произведений сгенерированы и записаны в файл library_books.json"


if __name__ == "__main__":
    main()

