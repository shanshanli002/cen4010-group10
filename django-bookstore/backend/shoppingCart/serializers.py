from pyexpat import model
from attr import fields
from idna import valid_label_length
from rest_framework import serializers
from shoppingCart.models import Cart

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("user", "item")

    #def create(validate_data):
        #cart = Cart.objects.create_cart(validate_data['user'], validate_data['item'])
        #return cart
    
    def save(self):
        cart = Cart(
            user = self.validated_data['user'],
            item = self.validated_data['item']
        )

        cart.save()
        return cart