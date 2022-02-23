from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ISBN_Search(request):
    """client view to search for book to view book details do not need model"""
   #without template ------     return HttpResponse("<h1> Hello World </h1>")
    return render (request, "ISBN_Search.html")

def Author_Books(request):
    """client view to search for books associated with a specific author do not need model"""
    return render(request, "Author_Books.html") 