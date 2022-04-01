from .models import Cart
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #model = User
        fields = ['id', 'name',]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'item']
