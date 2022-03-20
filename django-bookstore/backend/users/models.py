from django.db import models
from django.contrib.auth.models import User

    
class Users(models.Model):
   username = models.CharField(max_length = 100) 
   password = models.CharField(max_length =20 )  
   first_name = models.CharField(max_length=200)
   email=models.CharField(max_length = 200)  
  
   def __str__(self):
       return str(self.users)
    
