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
from books.views import *
urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('allbooks/', views.ISBN_Search),
    path('allauthors/', views.Author_Books),
    #api views
    path('books/', views.book_list),
    path('authors/', views.author_list),
    path('books/<int:ISBN>/', views.book_detail),
    path('books/<str:First_Name>/<str:Last_Name>/', views.author_books),
    path('books?Author=YannMartel', Author_Books.get_query)
]
