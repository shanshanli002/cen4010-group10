from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'Book_Description', 'Genre', 'Publisher', 'Year_Published', 'Copies_Sold', 'ISBN']
    
#condensed serializer compared to serializers.serializers, don't have to explicitly list all fields details, create, or update methods
#uses hyperlinks instead of primary keys
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['First_Name', 'Last_Name', 'Bio', 'Publisher']
