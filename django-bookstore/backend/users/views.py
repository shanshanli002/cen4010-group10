from django.shortcuts import render, redirect, HttpResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Users
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

#import stripe
#from knox.models import AuthToken



#from django.contrib.auth.forms import UserCreationForm
#from .forms import UserRegisterForm
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required


#def home(request):
 #   return render(request, 'users/home.html')


#def register(request):
   # if request.method == "POST":
   #     form = UserRegisterForm(request.POST)
   #     if form.is_valid():
   #         form.save()
   #         username = form.cleaned_data.get('username')
   #         messages.success(request, f'Hi {username}, your account was created successfully')
   #         return redirect('home')
    #else:
    #    form = UserRegisterForm()

    #return render(request, 'users/register.html', {'form': form})


#@login_required()
#def profile(request):
    #return render(request, 'users/profile.html')


#list all users 
@csrf_exempt
def List_All_Users(request):
    users = Users.objects.all()

    if request.method == 'GET':
        serializer = UserSerializer(users, many = True)
        return JsonResponse(serializer.data, status = 200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
  
@csrf_exempt 
#retrieve user information  
def User_Detail(request, username):
    try:
        username = Users.objects.get(username=username)

    except Users.DoesNotExist:
        raise Http404
         
    if request.method == 'GET':
        Users.objects.filter(Users = f'{First_Name}')
        serializer = UserSerializer(users, many = True)
        return JsonResponse(serializer.data, status = 200, safe=False)
      
    return JsonResponse(serializer.errors, status=400)

#update user information
@api_view(["PUT"])
@csrf_exempt
def put(self, request, username, first_name):
    try:
        users = Users.objects.filter(username=users, first_name=first_name)
      
        users.update(**payload)
        users = Users.objects.get(username=username)
        users = Users.objects.get(first_name=first_name)
        serializer = UsersSerializer(users)
        return JsonResponse({'users': serializer.data}, safe=False, status=200)
    
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=400)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=500)
     
     
'''
def Update_Users(request, username, first_name):
    users = request.users.id
    
    if request.method == 'PUT':
        serializer = UserSerializer(users, many = True)
        return JsonResponse(serializer.data, status = 200, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
    
    try:
        users = Users.objects.filter(username=users, first_name=first_name)
      
        users.update(**payload)
        users = Users.objects.get(username=username)
        users = Users.objects.get(first_name=first_name)
        serializer = UsersSerializer(users)
        return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_2010_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
'''