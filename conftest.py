import pytest
from books_collector import BooksCollector

@pytest.fixture
def collector():
    books_collector.add_new_book('Гордость и предубеждение и зомби')
    return BooksCollector()