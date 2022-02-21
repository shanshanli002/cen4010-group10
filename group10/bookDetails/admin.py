from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =('title','author', 'price', 'publisher', 'book_description', 'genre', 'year_published', 'copies_sold', 'ISBN')
    
    
admin.site.register(Book, BookAdmin)