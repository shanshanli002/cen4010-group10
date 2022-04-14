from django.db import models
from books.models import Book
from users.models import Customer

# Create your models here.                  

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
