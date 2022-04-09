from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework import request, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from users.models import Customer
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shoppingCart.form import shoppingCartForm
from shoppingCart.models import Cart

def all_items(request):
    cartItems = Cart.objects.all()
    return HttpResponse(cartItems)

@login_required
@require_POST
def submitCart(request):
    books = list(request.users.shoppingCart.all())
    request.users.books.add(*books)
    request.users.shoppingCartart.clear()
    request.users.save()

    for book in books:
        book.holders_count += 1
        book.save()

    return redirect("shoppingCart")

@login_required
@require_POST
def addToCart(request):
    form = shoppingCartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist:
        return redirect("/")

    request.users.shoppingCart.add(book)
    request.users.save()
    return redirect(form.cleaned_data.get("next_link"))

@login_required
@require_POST
def removeFromCart(request):
    form = shoppingCartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist:
        return redirect("/")

    request.users.shoppingCart.remove(book)
    request.users.save()
    return redirect(form.cleaned_data.get("next_link"))
       