import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_books_genre_is_empty(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_genre_has_all_genres(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    @pytest.mark.parametrize('book_name', ['', 'Тайна старого маяка на безлюдном острове!'])
    def test_add_new_book_length_0_and_41_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize('book_name, book_genre', [['Последний день Евы', 'Ужасы'], ['Щенячий дозор', 'Детективы']])
    def test_set_book_genre_valid_name_and_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == book_genre

    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Город снов')
        assert collector.get_book_genre('Город снов') == ''

    def test_get_book_genre_valid_name_returns_genre(self, collector_with_books):
        result = collector_with_books.get_book_genre('Город снов')
        assert result == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector_with_books):
        result = collector_with_books.get_books_with_specific_genre('Детективы')
        assert result == ['Щенячий дозор', 'Пуаро']

    def test_get_books_genre(self, collector_with_books):
        result = collector_with_books.get_books_genre()
        assert result == {'Щенячий дозор': 'Детективы', 'Город снов': 'Фантастика', 'Смех': 'Комедии', 'Пуаро': 'Детективы', 'Последний день Евы': 'Ужасы', 'Вверх!': 'Мультфильмы'}

    def test_get_books_for_children(self,collector_with_books):
        result = collector_with_books.get_books_for_children()
        assert result == ['Город снов', 'Смех', 'Вверх!']

    def test_add_book_in_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Вверх!')
        assert 'Вверх!' in collector_with_books.favorites

    def test_delete_book_from_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Пуаро')
        collector_with_books.delete_book_from_favorites('Пуаро')
        assert 'Пуаро' not in collector_with_books.favorites

    def test_get_list_of_favorites_books(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Смех')
        collector_with_books.add_book_in_favorites('Вниз!')
        result = collector_with_books.get_list_of_favorites_books()
        assert result == ['Смех']
