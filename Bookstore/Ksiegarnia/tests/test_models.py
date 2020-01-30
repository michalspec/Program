"""""from mixer.backend.django import mixer
import pytest
from django.contrib.auth.models import User

from Ksiegarnia.models import Book, Magazine


class TestModels:
    @pytest.mark.django_db
    def test_is_in_magazine(self):
        book = Book.objects.create(Title='Dawno temu', Author='Anonima',Price=12.41, Publisher='GigantMonopolowy')
        magazine = Magazine.objects.create(Amount =5, Book=book)
        assert magazine.is_in_magazine == True"""""
