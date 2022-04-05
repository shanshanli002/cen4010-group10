from django.db import models
from books.models import Book
from users.models import Users

class Comment(models.Model):
    #book = models.ForeignKey(Book, on_delete=models.CASCADE,default='Title') # foreign key from books used as a model 
    #user = models.ForeignKey(Users, on_delete=models.CASCADE,default='first_name') # foreign key from users used as a model 
    book = models.CharField(max_length = 500)
    user = models.CharField(max_length = 500) 
    body = models.CharField(max_length = 500) 
    rating = models.CharField(max_length = 500)
    date = models.DateField()
