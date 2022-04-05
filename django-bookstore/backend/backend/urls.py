"""authsysproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from users.views import *
from users import views
from django.urls import path
from django.urls import include
from books import views
from books.views import all_books, all_authors, book_list, author_list, book_detail
from users.views import List_All_Users

from bookRating.views import add_comment

urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
    #regular django views for book details 
    path('books/', all_books),
    path('authors/', all_authors),
    #api views for book details
    path('api/books/', book_list),
    path('api/authors/', author_list),
    path('api/books/<int:ISBN>/', book_detail),
    #api views for profile management
    path('users/',List_All_Users),
    #api views for book rating
    path('comments/',add_comment)
]
