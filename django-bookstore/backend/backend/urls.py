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
from django.urls import include, path
from users import views
#from payment import views
#from payment.views import *
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',views.List_All_Users),
    #api view
    path('users/<str:username>/',views.User_Detail),
    path('users/', views.put),
    path('creditcard/',views.List_All_CreditCard),
    #path('payment/', include('payment.urls')),
    #path('creditcard/',views.test_payment),
   
    
    #path('creditcard/', views.test_payment),
]
