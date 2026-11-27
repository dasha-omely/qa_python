import pytest
from main import BooksCollector
from data import BOOK_NAME, BOOK_GENRE, DET_GENRE, DET_BOOK_NAME, SECOND_DET_BOOK_NAME, COM_BOOK_NAME, CART_BOOK_NAME,COM_GENRE, HOR_GENRE, CART_GENRE

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_books_genre_is_empty(self, collector):
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('book_genre', [BOOK_GENRE, HOR_GENRE, DET_GENRE, CART_GENRE, COM_GENRE])
    def test_set_book_genre_allowed_genres(self, collector, book_genre):
        collector.add_new_book(BOOK_NAME)
        collector.set_book_genre(BOOK_NAME, book_genre)
        assert collector.get_book_genre(BOOK_NAME) == book_genre

    @pytest.mark.parametrize('book_name', ['', 'Тайна старого маяка на безлюдном острове!'])
    def test_add_new_book_length_0_and_41_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize('book_name, book_genre', [['Последний день Евы', 'Ужасы'], ['Щенячий дозор', 'Детективы']])
    def test_set_book_genre_valid_name_and_genre(self, collector, book_name, book_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == book_genre

    def test_get_book_genre_book_without_genre(self, collector):
        collector.add_new_book(BOOK_NAME)
        assert collector.get_book_genre(BOOK_NAME) == ''

    def test_get_book_genre_valid_name_returns_genre(self, collector):
        collector.add_new_book(BOOK_NAME)
        collector.set_book_genre(BOOK_NAME, BOOK_GENRE)
        result = collector.get_book_genre(BOOK_NAME)
        assert result == BOOK_GENRE

    def test_get_books_with_specific_genre(self, collector_for_genre_filter):
        result = collector_for_genre_filter.get_books_with_specific_genre(DET_GENRE)
        assert result == [DET_BOOK_NAME, SECOND_DET_BOOK_NAME]

    def test_get_books_genre(self, collector_for_genre_filter):
        result = collector_for_genre_filter.get_books_genre()
        assert result == {DET_BOOK_NAME: DET_GENRE, SECOND_DET_BOOK_NAME: DET_GENRE, BOOK_NAME: BOOK_GENRE}

    def test_get_books_for_children(self, collector_with_books):
        result = collector_with_books.get_books_for_children()
        assert result == [BOOK_NAME, COM_BOOK_NAME, CART_BOOK_NAME]

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book(BOOK_NAME)
        collector.add_book_in_favorites(BOOK_NAME)
        assert BOOK_NAME in collector.favorites

    def test_delete_book_from_favorites(self, collector_with_favorite):
        collector_with_favorite.delete_book_from_favorites(BOOK_NAME)
        assert BOOK_NAME not in collector_with_favorite.favorites

    def test_get_list_of_favorites_books(self, collector_with_favorite):
        result = collector_with_favorite.get_list_of_favorites_books()
        assert result == [BOOK_NAME]
