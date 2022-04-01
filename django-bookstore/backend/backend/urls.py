"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from books import views
from books.views import all_books, all_authors, all_genres, all_ratings, all_top_sellers, book_list, author_list, book_detail
urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
    #regular django views for book details 
    path('books/', all_books),
    path('authors/', all_authors),
    path('genres', all_genres),
    path('ratings', all_ratings),
    path('topsellers', all_top_sellers),
    #api views for book details
    path('api/books/', book_list),
    path('api/authors/', author_list),
    path('api/books/<int:ISBN>/', book_detail)
]
