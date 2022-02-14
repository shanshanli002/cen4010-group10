from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
import pyrebase
# Create your views here.

config = {
  "apiKey": "AIzaSyDY6UV8OBpaUuKdsUPdtvNwUxfZKPl4nMw",
  "authDomain": "profile-management-473b0.firebaseapp.com",
  "databaseURL": "https://profile-management-473b0-default-rtdb.firebaseio.com",
  "projectId": "profile-management-473b0",
  "storageBucket": "profile-management-473b0.appspot.com",
  "messagingSenderId": "64112140710",
  "appId": "1:64112140710:web:9ca806a20c3f34fc0aaf67",
  "measurementId": "G-JRMV1QMYTR"
}

# here we are doing firebase authentication
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# def index(request):
    # accessing our firebase data and storing it in a variable
    # email = database.child('data').child('email').get().val()
    # phone = database.child('data').child('phone').get().val()
    # userName = database.child('data').child('username').get().val()

    # context = {
       # 'email':email,
        # 'phone':phone,
       # 'userName':userName
    # }


def registerPage(request):
    	  if request.user.is_authenticated:
		            return redirect('home')
	      else:
		            form = CreateUserForm()
		            if request.method == 'POST':
			                  form = CreateUserForm(request.POST)
			                  if form.is_valid():
				                        form.save()
				                        user = form.cleaned_data.get('username')
				                        messages.success(request, 'Account was created for ' + user)

				                        return redirect('login')
			

		              context = {'form':form}
		              return render(request, 'templates/register.html', context)


def loginPage(request):
    	  if request.user.is_authenticated:
		            return redirect('home')
	      else:
		            if request.method == 'POST':
			                  username = request.POST.get('username')
			                  password =request.POST.get('password')

			                  user = authenticate(request, username=username, password=password)

			                  if user is not None:
				                        login(request, user)
				                        return redirect('home')
			                  else:
				                        messages.info(request, 'Username OR password is incorrect')

		              context = {}
		              return render(request, 'templates/login.html', context)

def logoutUser(request):
	      logout(request)
	      return redirect('login')
