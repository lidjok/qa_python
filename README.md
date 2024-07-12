# qa_python
1. Добавлен тест test_add_new_book_add_the_same_books
2. Добавляем тест test_set_book_genre_updates_books_genre(self) на проверку увеличения списка self.books_genre при вводе новых данных о книге
3. Добавляем тест test_get_book_genre_add_book_in_list_correct_gender(self) на проверку метода get_book_genre при вводе значения книги из списка
4. Добавлен тест test_get_books_with_specific_genre_genre_in_list_list для проверки метода get_books_with_specific_genre. При вводе жанра из списка
5. Добавлен тест test_get_books_genre_with_one_items_not_in_genre_list_without_items для проаерки метода get_books_genre, если передать книгу с жанром не из списка
6. Добавлен тест test_get_books_for_children_with_one_item_for_not_for_children_list_without_item для проверки выдачи списка без книг, имеющих ограничения возрастных
7. Добавлен тест test_add_book_in_favorites_valid_name_and_genre_list_with_item для проверки добавления в список favorites книги с валидным названием и жанром из списка
8. Добавлен тест test_add_book_in_favorites_with_book_not_in_list_list_NULL для проверки метода add_book_in_favorites при добавлении в список favorites книги не из списка
9. Добавлен тест test_add_book_in_favorites_with_two_books_the_same_list_just_one для проверки метода add_book_in_favorites при добавлении 2-х одинаковых книг
10. Добавлен тест test_delete_book_from_favorites_delete_only_book_list_empty для проверки метода def delete_book_from_favorites. Удаление единственной книги в списке