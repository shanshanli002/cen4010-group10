from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
#user account     
class Users(models.Model):
   username = models.CharField(max_length = 100) 
   password = models.CharField(max_length =20 )  
   first_name = models.CharField(max_length=200)
   email=models.CharField(max_length = 200)
   #number = models.CharField(max_length=13)
 
=======

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
<<<<<<< HEAD
    date_created=models.DateTimeField(auto_now_add=True,null=True)
>>>>>>> 74df3a7 (customer views)
=======
    password=models.CharField(max_length=200,null=True)
    card_info=models.CharField(max_length=200,null=True)
>>>>>>> 3376cec (created customer model and credit card)
    
    def __str__(self):
        return str(self.Customer)