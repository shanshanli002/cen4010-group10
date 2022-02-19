from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns=[
    #path('',home,name='home'),
    path('login/',loginPage,name='login'),
    path('register/',registerPage,name='register'),
    path('logout/',logoutPage,name='logout')
]