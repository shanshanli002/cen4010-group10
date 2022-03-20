from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import CreditCardSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def List_All_CreditCards(request):
    creditcard = CreditCard.objects.all()

    if request.method == 'GET':
        serializer = CreditCardSerializer(users, many = True)
        return JsonResponse(serializer.data, status = 200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    