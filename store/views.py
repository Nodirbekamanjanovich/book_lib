from rest_framework.viewsets import ModelViewSet
from store.models import Book
from store.serializer import BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
