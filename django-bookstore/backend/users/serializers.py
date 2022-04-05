from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import *



#user serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','user', 'name', 'email','password','card_info')
        extra_kwargs = {'password':{'write_only':True}}

 
def create(self, validated_data):
            Customer = Customer.objects.create_customer(validated_data['user'], validated_data['name'], validated_data['email'])
        
            return Customer
   