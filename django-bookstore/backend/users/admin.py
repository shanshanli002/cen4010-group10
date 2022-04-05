from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    #display for admin/users/accounts
    list_display=('id','user','name','email','password','card_info')
 

admin.site.register(Customer)

