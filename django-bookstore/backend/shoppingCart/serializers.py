from pyexpat import model
from attr import fields
from rest_framework import serializers
from shoppingCart.models import Cart

class cartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ("user", "item")