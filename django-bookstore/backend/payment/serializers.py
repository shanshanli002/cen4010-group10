from rest_framework import serializers
from django.contrib.auth.models import CreditCard
from .models import *

class CreditCard(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('id','cc_number','cc_expiry','cc_code','username')
        
    return CreditCard