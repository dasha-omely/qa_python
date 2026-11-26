import pytest
from main import BooksCollector

@pytest.fixture
def collector_with_books():
    collector = BooksCollector()

    collector.add_new_book('Щенячий дозор')
    collector.set_book_genre('Щенячий дозор', 'Детективы')

    collector.add_new_book('Город снов')
    collector.set_book_genre('Город снов', 'Фантастика')

    collector.add_new_book('Смех')
    collector.set_book_genre('Смех', 'Комедии')

    collector.add_new_book('Пуаро')
    collector.set_book_genre('Пуаро', 'Детективы')

    collector.add_new_book('Последний день Евы')
    collector.set_book_genre('Последний день Евы', 'Ужасы')

    collector.add_new_book('Вверх!')
    collector.set_book_genre('Вверх!', 'Мультфильмы')

    return collector
