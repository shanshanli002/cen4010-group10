from curses.ascii import HT
from unicodedata import name
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.views import APIView



class CustomerView(APIView):
    """
     View to list all users in the system.
    """
    permission_classes = (permissions.AllowAny,)
      
    def get(self, request, pk=None):
        """
        return a list of all users
        """
        customer = Customer.objects.all()
        if request.method == 'GET':
            serializer = CustomerSerializer(customer, many=True)
        
        return JsonResponse(serializer.data, status= 200, safe=False)
    
# Must be able to retrieve a User Object and its fields by their username
    def get_object(self,request,username):
        try:
            customer = Customer.objects.filter(username = ["username"])
        except Customer.DoesNotExist:
            return HttpResponse(status = 404)
       
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return JsonResponse(serializer.data, status = 201)
       
        elif request.method == 'DELETE':
            Customer.objects.filter(username = username).delete()
            return HttpResponse(status=204)
        
        
# Must be able to update the user and any of their fields except for mail  
# update the user information ex: name, email, address
    def put(self,request,pk=None):
        if request.method == 'PUT':
            customer = Customer.objects.all()
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    
 # Must be able to create a User with username(email), password and optional fields (name, email address, homeaddress)
 # Must be able to create Credit Card that belongs to a User
 # create a new user in the database
    def post(self, request, pk=None):
        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CustomerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
 
 
 
##Retrieve a list of cards for that user
class ListCards(APIView):       
  def get(self, request):
      customer = Customer.objects.all()
      if request.method == 'GET':
          serializer = CustomerSerializer(customer, many=True)
          return Response (
              {"username:":"ChampangePapi",
               "name" :"Drake Aubrey",
               "Chase: ": "Debit card ending in ...1234",
              "Visa:  ": "Debit card ending in ...1234"},status=200
              )
            
