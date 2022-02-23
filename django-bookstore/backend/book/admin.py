from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =('Title','Author','Genre','Book_Description','Price','Publisher','Year_Published','Copies_Sold','ISBN')
    
    
admin.site.register(Book, BookAdmin)
 
    
