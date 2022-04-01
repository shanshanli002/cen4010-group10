from django.contrib import admin
from .models import *

# Register your models here.

# model for user admin 
class UserAdmin(admin.ModelAdmin):
    #display for admin/users/accounts
    list_display=('id','username','password','first_name','email','number')
    
'''
# model for credit card admin 
class CardAdmin(admin.ModelAdmin):
    #display for admin/users/accounts
    list_display=('id','first_name','creditCard_number','creditCard_expiration','creditCard_code')
'''

admin.site.register(Users,UserAdmin)
#admin.site.register(Card,CardAdmin)
