from pickle import FALSE, TRUE
from django.db import models
from users.models import Customer
from books.models import Book
from django.db import models

# Create your models here.

class wishlistenitity(models.Model):

    wishlistuser = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="user")
    wishlistbook = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="book")
    wishlist = models.CharField(max_length=200)