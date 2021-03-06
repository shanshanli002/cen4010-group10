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
from bookSorting import views
from books.views import BooksRegular, BooksApi
from bookRating.views import CommentView, Average
from wishlist.views import WishlistView
from bookSorting.views import BookSortingGenreApi, BookSortingTopSellersApi, BookSortingRatingApi, BookSorting, ApiListView

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
    path(r'allcustomers/',CustomerView.as_view(),kwargs={'pk':None}),
    path(r'allcustomer/listcards/',ListCards.as_view()),
    #api views for shopping cart
    path('allCarts/', CartView.as_view(), kwargs={'pk': None}),
    path('addCartItem/', CartView.addToCart),
    path('removeCartItem/<str:user_id>/', CartView.removeFromCart),
    path('newCart/', CartView.createCart),
    path(r'allcustomer/<str:username>/',RetrieveUser.as_view()),
    #api views for book commenting and rating
    path('sorted/', CommentView.comments),
    path('newcomment/', CommentView.comments),
    path('sorted/<int:BookNum>/', CommentView.comments),
    path('avg/', Average.get_queryset),
    #api views for wishlist
    path('viewwishlist/', WishlistView.getWishList),
    path('removewishlist/<int:id>/',WishlistView.removefromwishlist),
    path('createwishlist/', WishlistView.createwishlist),
    #api views for book sorting
    path('api/genre/', BookSortingGenreApi.book_list),
    path('api/topsellers/', BookSortingTopSellersApi.book_list),
    path('api/rating/', BookSortingRatingApi.book_list),
    path('list/', ApiListView.as_view())
]
