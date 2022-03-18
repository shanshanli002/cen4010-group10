from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import BookSerializer
from .serializers import AuthorSerializer
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
#csrf allows for post without auth
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

@csrf_exempt
def book_detail(request, ISBN):
    try:
        book = Book.objects.get(ISBN = ISBN)

    except Book.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        Book.objects.filter(ISBN = ISBN).delete()
        return HttpResponse(status=204)

@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)