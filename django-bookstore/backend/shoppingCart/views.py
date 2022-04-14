from urllib import response
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from users.models import Customer
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shoppingCart.form import shoppingCartForm
from shoppingCart.models import Cart
from rest_framework.views import APIView
from shoppingCart.serializers import cartSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from books.models import Book

class CartView(APIView):
    @csrf_exempt
    def get(self, request, pk = None):
        cart = Cart.objects.all()
        if request.method == 'GET':
            serializer = cartSerializer(cart, many = True)
        return JsonResponse(serializer.data, status = 200, safe = False)

    @csrf_exempt
    def createCart(request):
        if  request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = cartSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            
            return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def addToCart(request, pk = None):
        if request.method == 'GET':
            cart = Cart.objects.all()
            serializer = cartSerializer(cart, data=request.data)
            if serializer.is_valid():
                serializer.save
                return JsonResponse(serializer.data, status = 201)
            return JsonResponse(serializer.errors, status = 400)
    
    @csrf_exempt
    def removeFromCart(request, user_id):
        if request.method == 'DELETE':
            Cart.objects.filter(user_id=user_id).delete()
            return HttpResponse(status = 204)
            
    