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
 
    def __str__(self):
        return str(self)
    
class Author(models.Model):
    First_Name = models.CharField(max_length=200,null=True)
    Last_Name = models.CharField(max_length=200,null=True)
    Bio = models.CharField(max_length=10000,null=True)
    Publisher = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self)

  


