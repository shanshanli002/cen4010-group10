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
from books.views import book_list, book_detail, author_list, all_books, all_authors
from users.views import List_All_Users

urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('allbooks/', all_books),
    path('allauthors/', all_authors),
    #api views for requests get and post 
    path('books/',book_list),
    path('authors/', author_list),
    path('books/<int:ISBN>/', book_detail),
    path('users/',List_All_Users)
]
