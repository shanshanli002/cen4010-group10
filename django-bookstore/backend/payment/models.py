from django.db import models
from django.contrib.auth.models import User
#from creditcard.models import CardNumberField, CardExpiryField, SecurityCodeField

#import stripe 

#create Credit Card that belongs to a User 

class Payment(models.Model):
    creditcard_number = models.CharField(max_length = 16) 
    creditcard_expiration = models.CharField(max_length =4)  
    credictcard_code = models.CharField(max_length=3)
    
    def __str__(self):
        return str(self.payment)
    
'''
class CreditCard(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    username = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.creditcard)
  
 '''
