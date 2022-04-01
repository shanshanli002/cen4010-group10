from django.contrib import admin
from .models import *

# Register your models here.

# model for user admin 
class UserAdmin(admin.ModelAdmin):
    #display for admin/users/accounts
    list_display=('id','username','password','first_name','email')
 

admin.site.register(Users,UserAdmin)

