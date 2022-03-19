from django.db import models
from django.contrib.auth.models import User
#from users.models import CardNumberField, CardExpiryField, SecurityCodeField
#import stripe 



#payments

#class Payment(models.Model):
  #  cc_number = CardNumberField(_('card number'))
  #  cc_expiry = CardExpiryField(_('expiration date'))
  #  cc_code = SecurityCodeField(_('security code'))
  #  user_name = models.CharField(max_length = 100) # required. username is going to be email sli078@fiu.edu   
    
class Users(models.Model):
   user_name = models.CharField(max_length = 100) # required. username is going to be email sli078@fiu.edu
   password = models.CharField(max_length =20 ) # required. Jidfsdfjisu!!#$
   name = models.CharField(max_length=200, null =True ) 
   home_address =models.CharField(max_length=200, null = True)  
   email_address=models.CharField(max_length = 200, null = True)   
    
   def __str__(self):
       return str(self.name)
    
