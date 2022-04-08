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
<<<<<<< HEAD
from users.views import List_All_Users, User_Detail
>>>>>>> 2a30d92 (retrieving user by certain id)
=======
#from users.views import List_All_Users
=======
from users.views import List_All_Customers,Customer_detail
>>>>>>> 3376cec (created customer model and credit card)
=======
#from users.views import List_All_Customers
>>>>>>> 41bd7c8 ( created get method to gather card infor for user)


>>>>>>> 74df3a7 (customer views)

urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    #regular django views for book details 
    path('books/', all_books),
    path('authors/', all_authors),
    #api views for book details
    path('api/books/', book_list),
    path('api/authors/', author_list),
    path('api/books/<int:ISBN>/', book_detail),
=======
    #regular django views for book details
    path('allbooks/', all_books),
    path('allauthors/', all_authors),
    #api views for book details 
    path('books/',book_list),
    path('authors/', author_list),
    path('books/<int:ISBN>/', book_detail),
    path(r'allcustomer/',CustomerView.as_view(),kwargs={'pk':None}),
    path(r'allcustomer/listcards/',ListCards.as_view())
    #path('allcustomer/',List_All_Customers)
>>>>>>> 41bd7c8 ( created get method to gather card infor for user)
    #api views for profile management
    #path('allcustomer/<str:pk>/',views.List_All_Customers, name="allcustomer"),
    #path('customer/<int:pk>/',Customer_detail),
    #path('customer/update/',post)
  
]
