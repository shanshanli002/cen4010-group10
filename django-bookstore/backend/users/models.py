from django.db import models
from django.contrib.auth.models import User

#user account     
class Users(models.Model):
   username = models.CharField(max_length = 100) 
   password = models.CharField(max_length =20 )  
   first_name = models.CharField(max_length=200)
   email=models.CharField(max_length = 200)
   cc_number = models.CharField(max_length=13)
  
   def __str__(self):
       return str(self.users)
    
'''
#credit card model
class Card(models.Model):
    first_name = models.CharField(max_length=100)
    creditCard_number = models.CharField(max_length=200)
    creditCard_expiration = models.CharField(max_length=4)
    creditCard_code = models.CharField(max_length=3)
    
    def __str__(self):
        return str(self)
    '''