from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from books.models import Book, Author
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Book
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


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

def all_book_list(request):
    """client view to search for books associated with a specific genre"""
    Book_List = Book.objects.all()
    return render(request, "Book_List.html", {'books': Book_List})

def all_genres(request):
    """client view to search for books associated with a specific genre"""
    Genre = Book.objects.all().order_by('Genre')
    return render(request, "Book_Genres.html", {'books': Genre})

def all_ratings(request):
    """client view to search for books associated with a specific genre"""
    Rating = Book.objects.all().order_by('Rating')
    return render(request, "Book_Ratings.html", {'books': Rating})

def all_top_sellers(request):
    """client view to search for books associated with a specific genre"""
    Copies_Sold = Book.objects.all().order_by('-Copies_Sold')
    return render(request, "Book_Top_Sellers.html", {'books': Copies_Sold})

#view for launching django app's home page
def homepage(request):
    return HttpResponse(f"Welcome to CEN4010 Group 10's Bookstore")

"""api views inlcude method: book_list, author_list, """
#csrf allows for post without auth
@csrf_exempt
def book_list(request):
    #returns all the books from db
    if request.method == 'GET':
        books = Book.objects.all()
        author_name = request.GET.get('Author')
        serializer = BookSerializer(books, many=True)
        #validate there was a query param 
        if author_name is not None:
            #validate the author name
            print(author_name)
            #chose to filter based on author name string vs author id because it's faster
            books = books.filter(Author=author_name)
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
        return JsonResponse(serializer.data, status = 201)
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
    #saving author json object to the db
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt
def book_list_top_sellers(request):
    #returns all the books from db
    if request.method == 'GET':
        books = Book.objects.all()
        author_name = request.GET.get('Author')
        serializer = BookSerializer(books, many=True)
        #validate there was a query param 
        if author_name is not None:
            #validate the author name
            print(author_name)
            #chose to filter based on author name string vs author id because it's faster
            books = books.filter(Author=author_name)
            serializer = BookSerializer(books, many=True)
        
        return JsonResponse(serializer.data, safe=False)