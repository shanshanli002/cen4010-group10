from django.db import models
from creditcard.models import CardNumberField, CardExpiryField, SecurityCodeField

from django.core import validators
#import stripe 

#create Credit Card that belongs to a User 
'''
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
  
 
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70,verbose_name='Product Name')
    description = models.TextField(max_length=800,verbose_name='Description')
    price = models.FloatField(verbose_name='Price',validators=[validators.MinValueValidator(50),validators.MaxValueValidator(100000)])