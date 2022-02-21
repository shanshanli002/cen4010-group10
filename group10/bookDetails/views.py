from django.http import HttpResponse
from django.shortcuts import render

def new_book(request):
    """admin view for adding new book"""
    return render(request, 'new_book/new_book.html',
         {'new_book':['title', 'author','book_description', 'genre', 'publisher', 1999, 18.90, 100, 123456]}) 

def ISBN_search(request):
    """client view to search for book to view book details"""
    return render(request, 'ISBN_search/ISBN_search.html', {'ISBN':[12345, 34567, 45678,0000,1010]}) 

def author(request):
    """admin view to add new author"""
    return render(request, 'author/author.html', {'author':['first', 'last', 'bio', 'publisher']}) 

def author_books(request):
    """client view to search for books associated with a specific author """
    return render(request, 'author_books/author_books.html', {'author_name': ['book1', 'book2', 'book3', 'book4']}) 

    