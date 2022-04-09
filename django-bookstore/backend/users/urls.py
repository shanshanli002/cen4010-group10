'''
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('allcustomer/<str:pk>/',views.List_All_Customers, name="allcustomer"),
]
'''
