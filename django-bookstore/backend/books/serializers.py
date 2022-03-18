from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'Book_Description', 'Genre', 'Publisher', 'Year_Published', 'Copies_Sold', 'ISBN']
    
#condensed serializer compared to serializers.serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['First_Name', 'Last_Name', 'Bio', 'Publisher']

