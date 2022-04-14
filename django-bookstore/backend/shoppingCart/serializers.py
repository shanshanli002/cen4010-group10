from rest_framework import serializers
from shoppingCart.models import Cart

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user_id', 'item_id'] 