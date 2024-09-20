#qa_python
Реализованные тесты
1. test_add_new_book_add_two_books
Описание: Проверяет возможность добавления двух книг в коллекцию.
Проверка: Убедиться, что две книги были добавлены и находятся в коллекции.
2. test_add_new_book
Описание: Проверяет добавление новой книги с разными именами.
Проверка: Убедиться, что книга успешно добавлена в коллекцию.
3. test_set_book_genre
Описание: Проверяет установку жанра для книги.
Проверка: Убедиться, что жанр корректно установлен для книги.
4. test_set_book_genre_for_non_existent_book
Описание: Проверяет попытку установить жанр для несуществующей книги.
Проверка: Убедиться, что попытка установки жанра для несуществующей книги не нарушает работу программы.
5. test_get_books_with_specific_genre
Описание: Проверяет получение списка книг с определённым жанром.
Параметры: Тестирует несколько случаев для разных жанров.
Проверка: Убедиться, что метод возвращает правильные книги для каждого жанра.
6. test_get_books_for_children
Описание: Проверяет получение списка книг, подходящих для детей.
Проверка: Убедиться, что книги с возрастными ограничениями не включаются в список детских книг.
7. test_add_book_in_favorites
Описание: Проверяет добавление книги в список избранных.
Проверка: Убедиться, что книга корректно добавляется в список избранных.
8. test_delete_book_from_favorites
Описание: Проверяет удаление книги из списка избранных.
Проверка: Убедиться, что книга корректно удаляется из списка избранных.
9. test_add_new_book_with_long_name
Описание: Проверяет добавление книги с названием, превышающим 40 символов.
Проверка: Убедиться, что книга с длинным названием не добавляется в коллекцию.
10. test_add_duplicate_book
Описание: Проверяет поведение при добавлении дубликатов книг.
Проверка: Убедиться, что одна и та же книга не добавляется дважды.
