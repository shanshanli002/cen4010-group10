from django.urls import path
from . import views

urlpatterns = [
    path('new_book/', views.new_book),
    path('ISBN_search/', views.ISBN_search),
    path('author/', views.author),
    path('author_books', views.author_books)
]    