from unittest import TestCase

from store.models import Book
from store.serializer import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name = 'Test book 1', price = 24.36)
        book_2 = Book.objects.create(name='Test book 2', price=16.87)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                "id" : book_1.id,
                "name" : 'Test book 1',
                "price" : '24.36'
            },
            {
                "id" : book_2.id,
                "name" : 'Test book 2',
                "price" : '16.87'
            }
        ]
        self.assertEqual(expected_data, data)