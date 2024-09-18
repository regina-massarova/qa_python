from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


import pytest

class TestBooksCollector:

    # Т
    @pytest.mark.parametrize("book_name", [
        ("Гарри Поттер и философский камень"),
        ("Властелин колец"),
        ("1984"),
    ])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1
        assert book_name in collector.get_books_genre()

    #
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер и философский камень') == 'Фантастика'

    #
    def test_set_book_genre_for_non_existent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Незарегистрированная книга', 'Фантастика')
        assert collector.get_book_genre('Незарегистрированная книга') is None

    #
    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Гарри Поттер и философский камень']),
        ('Ужасы', ['Сияние']),
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre(genre) == expected_books


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер и философский камень']


    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()


    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        long_name = 'Очень длинное название книги, которое превышает сорок символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('Гарри Поттер и философский камень')
        assert len(collector.get_books_genre()) == 1
