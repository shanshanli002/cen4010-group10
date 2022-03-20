from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    #display for admin/users/accounts
    list_display=('id','username','password','first_name','email_address','home_address')
    
admin.site.register(Users,UserAdmin)