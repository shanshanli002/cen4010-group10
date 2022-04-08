from curses.ascii import HT
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics


"""api views inlcude method: book_list, author_list, """
#csrf allows for post without auth
@csrf_exempt
def List_All_Customers(request):
    customer = Customer.objects.all()
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
def Customer_detail(customer):
    #check if the customer with the given name is in the database
    try:
        customer = Customer.objects.filter(name = name['name'])
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
