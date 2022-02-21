from django.db import models
from django.contrib.auth.models import User
from django.db import models

class new_book(models.Model):
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=200,null=True)
    book_description = models.CharField(max_length=10000,null=True)
    genre = models.CharField(max_length=200,null=True)
    publisher = models.CharField(max_length=200,null=True)
    year_published = models.IntegerField()
    price = models.FloatField()
    copies_sold = models.IntegerField()
    ISBN = models.IntegerField()
 
    def __str__(self):
        return str(self.title)

