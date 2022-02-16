from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =('title','Author', 'Price', 'Edition')
    
    
admin.site.register(Book, BookAdmin)