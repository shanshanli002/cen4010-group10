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
<<<<<<< HEAD
from books.views import all_books, all_authors, book_list, author_list, book_detail
from users.views import List_All_Users
=======
from books.views import book_list, book_detail, author_list, all_books, all_authors
<<<<<<< HEAD
<<<<<<< HEAD
from users.views import List_All_Users, User_Detail
>>>>>>> 2a30d92 (retrieving user by certain id)
=======
#from users.views import List_All_Users
=======
from users.views import List_All_Customers,Customer_detail
>>>>>>> 3376cec (created customer model and credit card)


>>>>>>> 74df3a7 (customer views)

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
    path('customer/',List_All_Customers),
    path('customer/<str:name>/',Customer_detail)
  
]
