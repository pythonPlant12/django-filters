from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response

from book.models import Book
from book.serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def list(self, request):
        books = Book.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data)