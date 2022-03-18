from django.shortcuts import render


# Create your views here.

#payments/views.py
stripe.api_key = 'sk_test_51KemoUGqfaDiaDObMk0fhdySSEOYxvFi5T6MMIaiDch7WFOqZA27pZZ14nUOszPvenNdqNKAg0Xp9udy6PJGVEpD000zvOjnxk'

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
    amount=1000, currency='pln', 
    payment_method_types=['card'],
    receipt_email='test@example.com')
    
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)