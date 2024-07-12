import pytest

from main import BooksCollector

@pytest.fixture()
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_book():
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector