from django.urls import path, include
from django.contrib.auth import views 
from .views import *


urlpatterns=[
    path('', home,name='home'),
    path('login/', loginPage,name='login'),
    path('viewcart/', viewcart,name='viewcart'),
    path('addbook/', addbook,name='addbook'),
    path('register/', registerPage,name='register'),
    path('logout/', logoutPage,name='logout'),
    path('addtocart/<str:pk>', addtocart,name='addtocart'), 
    
]