from django.db import models
from books.models import Book
from users.models import Users

class Comment(models.Model): # comment model described as a model 
    book = models.ForeignKey(Book, on_delete=models.CASCADE,default='Title') # foreign key from books used as a model 
    user = models.ForeignKey(Users, on_delete=models.CASCADE,default='first_name') # foreign key from users used as a model 
    body = models.TextField(max_length=500) # text field that will be used for the comment 
    date = models.DateTimeField(auto_now_add=True) # the time at which user made the comment 
    rating = models.CharField(max_length=10)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)