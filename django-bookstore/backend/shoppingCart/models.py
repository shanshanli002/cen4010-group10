from django.db import models
from book.models import Book

# Create your models here.                  

class Cart(models.Model):
    #user = models.ForeignKey(UserID, on_delete=models.SET_NULL) 
    item = models.ForeignKey(Book, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self)
                                               
                                               