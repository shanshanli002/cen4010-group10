'''
class CreditCard(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('id','cc_number','cc_expiry','cc_code','username')
  '''  