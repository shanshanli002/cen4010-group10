from crypt import methods
from webbrowser import get
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import request, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart 
from .serializer import UserSerializer, CartSerializer 
from django.http import HttpResponse, JsonResponse
from users.models import Users
from django.views.decorators.csrf import csrf_exempt
from books.models import Book


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UserSerializer

@csrf_exempt
def cartItems(request):
        if request.method == ('GET'):
           allBooks = Cart.objects.all()
           serializer = CartSerializer(allBooks , many = True)
           return JsonResponse(serializer.data, status = 200, safe=False)

@api_view(['PUT'])
@csrf_exempt    
def addBook(request, pk):
        if request.method == ('PUT'):
            return
        

@csrf_exempt  
def deleteItem(self, request, pK = None):
        if request.method == ('DELETE'):
            Cart.objects.filter(item = item)

       