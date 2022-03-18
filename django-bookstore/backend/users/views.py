from django.shortcuts import render, redirect, HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from .models import *
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


#register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
