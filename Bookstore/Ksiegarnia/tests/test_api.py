import pytest

from Ksiegarnia.models import Book

@pytest.mark.django_db
def test__add_book():
    data_to_save = {
        'Title' : 'Dawno temu',
        'Author' : 'Anonima',
        'Price' : 12.41,
        'Publisher' : 'GigantMonopolowy'
    }

    url = reversed('book')

    all_book = Book.objects.all()
    assert all_book.count == 3

    saved_book = all_book.first()
    assert saved_book.Title == 'Malma'