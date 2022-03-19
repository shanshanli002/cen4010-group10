from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# user registeration below 
#user serializer
#class UserSerializer(serializers.ModelSerializer):
   # class Meta:
    #    model = Usesr
    #    fields = ('id', 'username', 'email')
    #    depth = 1
        

        
#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','password','name', 'email_address', 'home_address' )
        #extra_kwargs = {'password': {'write_only': True}}
        
    
    #def create(self, validated_data):
        #user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

       # return user

