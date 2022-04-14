from curses.ascii import HT
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from books.models import Book, Author
from rest_framework import generics
from wishlist.models import wishlistenitity
from wishlist.serializers import WishlistSerializer
from rest_framework.views import APIView

class WishlistView(APIView):

    # view Wishlist
    def get(request, pk=None):
        ViewWishlist = wishlistenitity.objects.all()
        if request.method == 'GET':
            #serializer = WishlistSerializer(ViewWishlist, many=True)
            return HttpResponse(ViewWishlist, status= 200)
        else: 
            return HttpResponse(ViewWishlist, status= 400)