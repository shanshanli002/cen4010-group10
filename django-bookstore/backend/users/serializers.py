from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

#user serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ('id','user', 'name', 'email','address','password','card_info')
=======
        fields = ('id','user', 'name', 'email','password','card_info')
>>>>>>> ef66e24 (renamed user to customer to be able to create a credit card)
=======
        fields = ('id','user', 'name', 'email','address','password','card_info')
>>>>>>> 2186330 (added address to user form)
        extra_kwargs = {'password':{'write_only':True}}

 
def create(self, validated_data):
            customer = Customer.objects.create_customer(validated_data['user'], validated_data['name'], validated_data['email'])
        
            return customer
   