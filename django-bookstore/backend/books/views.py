from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def ISBN_Search(request):
    """client view to search for book to view book details do not need model"""
   #without template ------     return HttpResponse("<h1> Hello World </h1>")
    # var books = use name of model to retrieve from DB
    books = Book.objects.all()
    return render (request, "ISBN_Search.html", {'all_books': books})

def Author_Books(request):
    """client view to search for books associated with a specific author do not need model"""
    authors = Author.objects.all()
    return render(request, "Author_Books.html", {'all_authors': authors}) 