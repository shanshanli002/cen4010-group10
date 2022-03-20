from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class Payment(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','creditcard_number','creditcard_expiration','creditcard_code']
        
def create(self, validated_data):
    return Payment.objects.create(validated_data)