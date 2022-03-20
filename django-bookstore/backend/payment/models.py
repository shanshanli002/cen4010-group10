from django.db import models
#from creditcard.models import CardNumberField, CardExpiryField, SecurityCodeField

#import stripe 

#create Credit Card that belongs to a User 

class CreditCard(models.Model):
    cc_number = models.CharField(max_length = 100) 
    cc_expiry = models.CharField(max_length =20 )  
    cc_code = models.CharField(max_length=3)
    username = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.creditcard)
    
'''
class CreditCard(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    username = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.creditcard)
  
 '''
