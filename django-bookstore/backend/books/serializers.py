from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['Title', 'Author', 'Price', 'Book_Description', 'Genre', 'Publisher', 'Year_Published', 'Copies_Sold', 'ISBN']
    

#creating a serializer with condensed code compared to the top 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['First_Name', 'Last_Name', 'Bio', 'Publisher']

