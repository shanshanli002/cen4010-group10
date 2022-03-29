from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics


"""regular django views to view all books and all authors include methods: all_books and all_authors"""
def all_books(request):
    """client view to search for book to view book details do not need model"""
   #without template ------     return HttpResponse("<h1> Hello World </h1>")
    # var books = use name of model to retrieve from DB
    books = Book.objects.all()
    return render (request, "ISBN_Search.html", {'books': books})

def all_authors(request):
    """client view to search for books associated with a specific author do not need model"""
    authors = Author.objects.all()
    return render(request, "Author_Books.html", {'authors': authors}) 
#view for launching django app's home page
def homepage(request):
    return HttpResponse('Welcome to Bookstore')

"""api views inlcude method: book_list, author_list, """
#csrf allows for post without auth
@csrf_exempt
def book_list(request):
    #returns all the books from db
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    #add new book in the db
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_detail(request, ISBN):
    #check if the book with the given isbn is in the database
    try:
        book = Book.objects.get(ISBN = ISBN)
    #if not in database, throw 400 error 
    except Book.DoesNotExist:
        return HttpResponse(status = 404)
    #if book exists with the given ISBN and is a get method, return that book object which is the book variable
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    #delete method will delete the book with a specific isbn
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