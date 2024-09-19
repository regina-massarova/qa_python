import pytest
from main import BooksCollector  # Подключаем класс BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", [
        'Гарри Поттер и философский камень',
        'Властелин колец',
        '1984',
    ])
    def test_add_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1
        assert book_name in collector.get_books_genre()

    def test_set_book_genre(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

    def test_set_book_genre_for_non_existent_book(self, collector):
        collector.set_book_genre('Незарегистрированная книга', 'Фантастика')
        assert collector.get_book_genre('Незарегистрированная книга') is None

    @pytest.mark.parametrize("books, genres, target_genre, expected_books", [
        (['Гарри Поттер и философский камень', 'Сияние'], ['Фантастика', 'Ужасы'], 'Фантастика', ['Гарри Поттер и философский камень']),
        (['Гарри Поттер и философский камень', 'Сияние'], ['Фантастика', 'Ужасы'], 'Ужасы', ['Сияние']),
        (['Гарри Поттер и философский камень', 'Сияние'], ['Фантастика', 'Ужасы'], 'Детективы', []),
    ])
    def test_get_books_with_specific_genre(self, collector, books, genres, target_genre, expected_books):
        # добавляем книги и устанавливаем им жанры
        for book, genre in zip(books, genres):
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        # проверяем, что для целевого жанра возвращаются нужные книги
        assert collector.get_books_with_specific_genre(target_genre) == expected_books

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер и философский камень']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()

    def test_add_new_book_with_long_name(self, collector):
        long_name = 'Очень длинное название книги, которое превышает сорок символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_duplicate_book(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Гарри Поттер и философский камень')
        assert len(collector.get_books_genre()) == 1
