from django.db import models
from books.models import Book
from users.models import Users

# Create your models here.                  

class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL) 
    item = models.ForeignKey(Book, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self)
                                               
                                               