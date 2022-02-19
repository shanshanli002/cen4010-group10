from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =('title','Author', 'Price', 'Edition')
    
class CustomerAdmin(admin.ModelAdmin):
    user_infor=('user','name','phone','email','date_created')
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Customer)