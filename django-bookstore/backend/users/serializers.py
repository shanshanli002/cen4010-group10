from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','cc_number')
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['first_name'])

        return user
'''
#credit card serializer 
class Card(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'first_name','creditCard_nummber', 'creditCard_expiration', 'creditCard_code')
        '''