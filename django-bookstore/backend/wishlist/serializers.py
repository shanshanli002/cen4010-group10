from rest_framework import serializers
from books.models import Book
from books.models import Author
from wishlist.models import wishlistenitity 

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = wishlistenitity
        fields = ['wishlistuser', 'wishlistbook', 'wishlist']
    

