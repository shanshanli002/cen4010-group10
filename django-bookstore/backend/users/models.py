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
    user=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
<<<<<<< HEAD
<<<<<<< HEAD
    date_created=models.DateTimeField(auto_now_add=True,null=True)
>>>>>>> 74df3a7 (customer views)
=======
=======
    address=models.CharField(max_length=200,null=True)
>>>>>>> 003a6df (created url path and customer model)
    password=models.CharField(max_length=200,null=True)
    card_info=models.CharField(max_length=200,null=True)
>>>>>>> 3376cec (created customer model and credit card)
    
    def get_user(self):
        return self.user
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def get_password(self):
        return self.password
    def get_card_info(self):
        return self.card_info
   
        
        
        