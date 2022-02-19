from dataclasses import field
from rest_framework import serializers
from .models import Customer, Book, Cart

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'Author', 'Price','Edition')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'user','name','phone','email','date_created')
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'customer', 'book')