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
from shoppingCart.views import CartView
from users import views
from django.urls import path
from django.urls import include
from books import views
from books.views import BooksRegular, BooksApi
from bookRating.views import CommentView, Average


urlpatterns = [
    #regular views for the django app
    path('', BooksRegular.homepage),
    path('admin/', admin.site.urls),
    #regular django views for book details 
    path('books/', BooksRegular.all_books),
    path('authors/', BooksRegular.all_authors),
    #api views for book details
    path('api/books/', BooksApi.book_list),
    path('api/authors/', BooksApi.author_list),
    path('api/books/<int:ISBN>/', BooksApi.book_detail),
    #api views for profile management
    path(r'allcustomer/',CustomerView.as_view(),kwargs={'pk':None}),
    path(r'allcustomer/listcards/',ListCards.as_view()),
    #api views for shopping cart
    path('allCarts/', CartView.as_view(), kwargs={'pk': None}),
    path('addCartItem/', CartView.addToCart),
    path('removeCartItem/<str:user_id>/', CartView.removeFromCart),
    path('newCart/', CartView.createCart),
    #api views for book commenting and rating
    path('sorted/', CommentView.comments),
    path('avg/', Average.get_queryset),
    path('newcomment/', CommentView.comments),
    path('sorted/<int:BookNum>/', CommentView.comments)
]
