from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

class ProductListView(ListView):
    pass


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "payments/product_create.html"
    success_url = reverse_lazy("home")


class ProductDetailView(DetailView):
    pass

@csrf_exempt
def create_checkout_session(request, id):
	pass


class PaymentSuccessView(TemplateView):
    pass

class PaymentFailedView(TemplateView):
    pass

class OrderHistoryListView(ListView):
    pass