from django.contrib import admin
from .models import *

# model for credit card admin

class CreditCardAdmin(admin.ModelAdmin):
    list_display=('id','cc_number','cc_expiry','cc_code','username')
 
 
admin.site.register(CreditCard,CreditCardAdmin)