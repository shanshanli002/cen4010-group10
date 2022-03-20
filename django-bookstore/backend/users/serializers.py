from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



#user serializer
      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'email_address', 'home_address' )
        #extra_kwargs = {'password': {'write_only': True}}
        
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email_address'], validated_data['password'])
        user.save()

        return user

