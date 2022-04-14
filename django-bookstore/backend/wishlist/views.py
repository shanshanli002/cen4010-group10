from curses.ascii import HT
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from books.models import Book, Author
from rest_framework import generics
from wishlist.models import wishlistenitity
from wishlist.serializers import WishlistSerializer
from rest_framework.views import APIView

class WishlistView():
    # view Wishlist
    def getWishList(request, pk=None):
        if request.method == 'GET':
            wishlistobjects = wishlistenitity.objects.all()
            serializer = WishlistSerializer(wishlistobjects, many=True)
            return JsonResponse(serializer.data, safe=False)