from pickle import FALSE, TRUE
from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Price = models.FloatField()
    Book_Description = models.CharField(max_length=10000)
    Genre = models.CharField(max_length=200)
    Publisher = models.CharField(max_length=200)
    Year_Published = models.IntegerField()
    Copies_Sold = models.IntegerField()
    ISBN = models.IntegerField()
    #Ratings = models.IntegerField()
 
class Author(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Bio = models.CharField(max_length=10000)
    Publisher = models.CharField(max_length=200)