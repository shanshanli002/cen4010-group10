from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #display for admin/book/book/
    list_display =('ISBN','Title','Author','Genre','Book_Description','Price','Publisher','Year_Published','Copies_Sold')
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Bio', 'Publisher')    

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
 
    
