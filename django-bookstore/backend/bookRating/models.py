from django.db import models
#from django.contrib.auth.models import Book
#from django.contrib.auth.models import User


class Comments(models.Model): # comment model described as a model 
    #book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='comments') # foreign key from books used as a model 
    #user = models.ForeignKey(User, on_delete=models.CASCADE) # foreign key from users used as a model 
    book = models.CharField(max_length=200)
    userz = models.CharField(max_length=200)
    body = models.TextField() # text field that will be used for the comment 
    date = models.DateTimeField(auto_now_add=True) # the time at which user made the comment 
    rating = models.IntField(max_length=1)

    class Meta:
        ordering = ['date']

