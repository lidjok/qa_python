from main import BooksCollector


def test_add_new_book_the_same_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    assert len(collector.books_genre) == 1


def test_set_book_genre_updates_books_genre(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    assert len(collector.books_genre) == 1


def test_get_book_genre_add_book_in_list_correct_gender(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'


def test_get_books_with_specific_genre_genre_in_list_list(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    assert collector.get_books_with_specific_genre('Комедии') == [
        'Гордость и предубеждение и зомби']


def test_get_books_genre_with_one_items_not_in_genre_list_without_items(collector):
    collector.add_new_book('Война и мир')
    assert collector.get_book_genre('Война и мир') == ''

def test_get_books_for_children_with_one_item_for_not_for_children_list_without_item(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    collector.add_new_book('Агата Кристи')
    collector.set_book_genre('Агата Кристи', 'Детективы')
    assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']  # Исправлено: возвращается список


def test_add_book_in_favorites_valid_name_and_genre_list_with_item(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    assert collector.favorites == ['Гордость и предубеждение и зомби']  # Исправлено: возвращается список


def test_add_book_in_favorites_with_book_not_in_list_list_null(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    collector.add_book_in_favorites('Понедельник начинается в субботу')
    assert collector.favorites == []


def test_add_book_in_favorites_with_two_books_the_same_list_just_one(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    assert len(collector.favorites) == 1


def test_delete_book_from_favorites_delete_only_book_list_empty(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
    assert collector.favorites == []