from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



#user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name')
        extra_kwargs = {'password': {'write_only': True}}
   
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['first_name'])

        return user

    