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
  
  

  
  #update the user information ex: name, email, address
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
 
 
 ##Retrieve a list of cards for that user
class ListCards(APIView):       
  def get(self, request):
      customer = Customer.objects.all()
      if request.method == 'GET':
          serializer = CustomerSerializer(customer, many=True)
          return Response (
              {"user:":"ChampangePapi",
               "name" :"Drake Aubrey",
               "Chase: ": "Debit card ending in ...1234",
              "Visa:  ": "Debit card ending in ...1234"},status=200
              )
            
       
        
      
    
'''
#csrf allows for post without auth
@csrf_exempt
def List_All_Customers(request,pk):
    customer = Customer.objects.get(pk=pk)
    
    #returns all the customer from db
    if request.method == 'GET':
        serializer = CustomerSerializer(customer, many=True)
        
        return JsonResponse(serializer.data, status= 200, safe=False)
    #add new customer in the db
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Customer_detail(request,pk):
    #check if the customer with the given name is in the database
   
    try:
        customer = Customer.objects.get(pk=pk)
            
    #if not in database, throw 400 error 
    except Customer.DoesNotExist:
        return HttpResponse(status = 404)
    #if customer exists with the given name and is a get method, return that name object 
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)
    #delete method will delete the customer with a specific name
    elif request.method == 'DELETE':
        Customer.objects.filter(name = name).delete()
        return HttpResponse(status=204)
 

def get (request):
    if request.method == 'GET':
        customer = request.customer.id
        print (customer)
           
'''  


 
        
      