from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=200)
    Author = serializers.CharField(max_length=200)
    Price = serializers.FloatField()
    Book_Description = serializers.CharField(max_length=10000)
    Genre = serializers.CharField(max_length=200)
    Publisher = serializers.CharField(max_length=200)
    Year_Published = serializers.IntegerField()
    Copies_Sold = serializers.IntegerField()
    ISBN = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Author = validated_data.get('Author', instance.Author)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Book_Description = validated_data.get('Book_Description', instance.Book_Description)
        instance.Genre = validated_data.get('Genre', instance.Genre)
        instance.Publisher = validated_data.get('Publisher', instance.Publisher)
        instance.Year_Published = validated_data.get('Year_Published', instance.Year_Published)
        instance.Copies_Sold = validated_data.get('Copies_Sold', instance.Copies_Sold)
        instance.ISBN = validated_data.get('ISBN', instance.ISBN)
        instance.save()
        return instance

#creating a serializer with condensed code compared to the top 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['First_Name', 'Last_Name', 'Bio', 'Publisher']

