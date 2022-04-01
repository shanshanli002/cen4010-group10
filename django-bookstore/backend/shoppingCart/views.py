from webbrowser import get
from rest_framework import viewsets
from rest_framework import request, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart 
from .serializer import UserSerializer, CartSerializer 
from django.http import HttpResponse



class UserView(viewsets.ModelViewSet):
    #queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class CartView(viewsets.ModelViewSet):
    def cartItems(request):
        if request.method == ('GET'):
            queryset = Cart.objects.all()
            serializer_class = CartSerializer
        
            return queryset
    
    def deleteItem(request):
        if request.method == ('DELETE'):
            queryset = Cart.objects.all().order_by('id')
            serializer_class = CartSerializer

            return queryset

       