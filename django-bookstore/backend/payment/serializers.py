from rest_framework import serializers
from .models import *

class CreditCard(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('id','cc_number','cc_expiry','cc_code','username')
        
    return CreditCard