from django.db import models

from author.models import Author

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    author = models.ForeignKey(to=Author, related_name='author', on_delete=models.CASCADE)
    