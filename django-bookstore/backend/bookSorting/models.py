from django.db import models
from books.models import Book
from bookRating.models import Comment
from users.models import Customer
from django.db.models import Avg
from pickle import FALSE, TRUE
from django.contrib.auth.models import User

class Sorting(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Price = models.FloatField()
    Book_Description = models.CharField(max_length=10000)
    Genre = models.CharField(max_length=200)
    Publisher = models.CharField(max_length=200)
    Year_Published = models.IntegerField()
    Copies_Sold = models.IntegerField()
    score = models.IntegerField(choices=((1,"*"),(2, "**"), (3, "***"), (4, "****"), (5, "*****")))
    ISBN = models.IntegerField()