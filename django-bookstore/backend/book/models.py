from django.db import models
from django.contrib.auth.models import User


from django.db import models


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200,null=True)
    Author=models.CharField(max_length=200,null=True)
    Price=models.IntegerField()
    Edition=models.IntegerField()
 
    def __str__(self):
        return str(self.title)
<<<<<<< HEAD
<<<<<<< HEAD
    
=======
    
>>>>>>> parent of 1662163 (Merge pull request #4 from shanshanli002/bookSorting)
=======
    
>>>>>>> parent of 1662163 (Merge pull request #4 from shanshanli002/bookSorting)
