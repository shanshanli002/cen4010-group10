from curses.ascii import HT
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from books.models import Book, Author
from rest_framework import generics
from wishlist.models import wishlistenitity
from wishlist.serializers import WishlistSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


class WishlistView():
    # view Wishlist
    def getWishList(request, pk = None):
        if request.method == 'GET':
            wishlistobjects = wishlistenitity.objects.all()
            serializer = WishlistSerializer(wishlistobjects, many=True)
            return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def removefromwishlist(request, id):
        if request.method == 'DELETE':
            wishlistenitity.objects.filter(id = id).delete()
            return HttpResponse(status = 204)

    @csrf_exempt
    def createwishlist(request):
        if  request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = WishlistSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

            return JsonResponse(serializer.errors, status=400)