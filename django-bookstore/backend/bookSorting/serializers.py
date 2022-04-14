
from rest_framework import serializers
from bookSorting.models import Sorting
from bookRating.models import Comment
from books.models import Book
from django.db.models import Avg


class BookSortingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'Genre', 'Publisher', 'Year_Published', 'Copies_Sold', 'ISBN']


class BookSortingRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'book', 'score', 'title',]