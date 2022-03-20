from django.db import models
from django.contrib.auth.models import User
#from users.models import CardNumberField, CardExpiryField, SecurityCodeField
#import stripe 



#payments
'''
class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    username = models.CharField(max_length = 100) # required. username is going to be 
   '''
    
class Users(models.Model):
   username = models.CharField(max_length = 100) 
   password = models.CharField(max_length =20 )  
   first_name = models.CharField(max_length=200)
   email=models.CharField(max_length = 200)  

     
    
   def __str__(self):
       return str(self.users)
    
