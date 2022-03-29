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
<<<<<<< HEAD
from django.urls import path, include
from users import views
#from payment import views
#from payment.views import *
from users.views import *


=======
from django.urls import path
from django.urls import include
from books import views
from books.views import *
>>>>>>> main
urlpatterns = [
    #regular views for the django app
    path('', views.homepage),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('users/',views.List_All_Users),
    #path('usersDetail/<str:username>/',views.User_Detail),
    #path('users/',views.Update_User),
    #path('users/',views.Delete_User),
    
=======
    path('allbooks/', views.all_books),
    path('allauthors/', views.all_authors),
    #api views for requests get and post 
    path('books/', views.book_list),
    path('authors/', views.author_list),
    path('books/<int:ISBN>/', views.book_detail)
>>>>>>> main
]
