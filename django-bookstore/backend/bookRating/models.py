from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Book


class Comments(models.Model): # comment model described as a model 
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # foreign key from books used as a model 
    user = models.ForeignKey(User, on_delete=models.CASCADE) # foreign key from users used as a model 
    body = models.TextField() # text field that will be used for the comment 
    date = models.DateTimeField(auto_now_add=True) # the time at which user made the comment 
    rating = models.IntField(max_length=1)


#    def __str__(self):
#        return '{} - {}'.format(self.livre.title, self.user)
