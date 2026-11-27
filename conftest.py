import pytest
from main import BooksCollector
from data import BOOK_NAME, BOOK_GENRE, DET_BOOK_NAME, SECOND_DET_BOOK_NAME, DET_GENRE, COM_BOOK_NAME, COM_GENRE, HOR_BOOK_NAME, HOR_GENRE, CART_BOOK_NAME, CART_GENRE

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_for_genre_filter(collector):

    collector.add_new_book(DET_BOOK_NAME)
    collector.set_book_genre(DET_BOOK_NAME, DET_GENRE)

    collector.add_new_book(SECOND_DET_BOOK_NAME)
    collector.set_book_genre(SECOND_DET_BOOK_NAME, DET_GENRE)

    collector.add_new_book(BOOK_NAME)
    collector.set_book_genre(BOOK_NAME, BOOK_GENRE)

    return collector

@pytest.fixture
def collector_with_books(collector):

    collector.add_new_book(BOOK_NAME)
    collector.set_book_genre(BOOK_NAME, BOOK_GENRE)

    collector.add_new_book(DET_BOOK_NAME)
    collector.set_book_genre(DET_BOOK_NAME, DET_GENRE)

    collector.add_new_book(COM_BOOK_NAME)
    collector.set_book_genre(COM_BOOK_NAME, COM_GENRE)

    collector.add_new_book(HOR_BOOK_NAME)
    collector.set_book_genre(HOR_BOOK_NAME, HOR_GENRE)

    collector.add_new_book(CART_BOOK_NAME)
    collector.set_book_genre(CART_BOOK_NAME, CART_GENRE)

    return collector

@pytest.fixture
def collector_with_favorite(collector):
    collector.add_new_book(BOOK_NAME)
    collector.add_book_in_favorites(BOOK_NAME)
    return collector
