from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
from rest_framework import viewsets
from .serializers import BookSerializer, CustomerSerializer, CartSerializer
from .forms import *

# Create your views here.

# redirect customer to main page when logged out
def logoutPage(request):
    logout(request)
    return redirect('/')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                print("working")
                login(request,user)
                return redirect('/')
            context={}
            return render(request,'book/login.html',context)

def registerPage(request):
    form=createuserform()
    cust_form=createcustomerform()
    if request.method=='POST':
        form=createuserform(request.POST)
        cust_form=createcustomerform(request.POST)
        if form.is_valid() and cust_form.is_valid():
            user=form.save()
            customer=cust_form.save(commit=False)
            customer.user=user
            customer.save()
            return redirect('login')
        context={
            'form':form,
            'cust_form':cust_form,
        }
        return render (request,'book/register.html',context)
    