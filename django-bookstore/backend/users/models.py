from django.db import models
from users.models import CardNumberField, CardExpiryField, SecurityCodeField
import stripe 


# Create your models here.
#payments

class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    
