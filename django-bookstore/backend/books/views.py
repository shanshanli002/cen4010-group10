from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from.serializers import *
from django.views.decorators.csrf import csrf_exempt

# these are regular django views
def ISBN_Search(request):
    """client view to search for book to view book details do not need model"""
   #without template ------     return HttpResponse("<h1> Hello World </h1>")
    # var books = use name of model to retrieve from DB
    books = Book.objects.all()
    return render (request, "ISBN_Search.html", {'books': books})

def Author_Books(request):
    """client view to search for books associated with a specific author do not need model"""
    authors = Author.objects.all()
    return render(request, "Author_Books.html", {'authors': authors}) 

def homepage(request):
    return HttpResponse('Welcome to Bookstore')
@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)