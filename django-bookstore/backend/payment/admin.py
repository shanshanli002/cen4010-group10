from django.contrib import admin
from .models import *

# model for credit card admin

class PaymentAdmin(admin.ModelAdmin):
    list_display=('id','creditcard_number','creditcard_expiration','creditcard_code')
 
 
admin.site.register(Payment,PaymentAdmin)