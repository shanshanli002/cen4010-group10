from django.db.models import Avg
from django.forms import CharField
from bookSorting.models import Sorting
from books.models import Book
from bookRating.models import Comment
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from bookSorting.serializers import BookSortingSerializer, BookSortingRatingSerializer
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookSortingGenreApi(APIView):
    @csrf_exempt
    # get bookratings by sort highest to lowest 
    def book_list(request):
        #returns all the books from db
        if request.method == 'GET':
            books = Book.objects.all()
            genre_name = request.GET.get('Genre')
            serializer = BookSortingSerializer(books, many=True)
            #validate there was a query param 
            if genre_name is not None:
                #validate the genre name
                print(genre_name)
                #chose to filter based on author name string vs genre because it's faster
                books = books.filter(Genre=genre_name)
                serializer = BookSortingSerializer(books, many=True)
        
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = BookSortingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

class BookSortingTopSellersApi(APIView):
    @csrf_exempt
    # get bookratings by sort highest to lowest 
    def book_list(request, pk=None):
        sort = Book.objects.all().order_by('-Copies_Sold')[:10]
        if request.method == 'GET':
            serializer = BookSortingSerializer(sort, many=True)
            return JsonResponse(serializer.data, status= 200, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = BookSortingSerializer(data=data)
            #check if all fields are present
            if serializer.is_valid():
                #save the object to the db
                serializer.save()
                #display the new book comment, rating, and timestamp to the user
                return JsonResponse(serializer.data, status = 201)

class BookSortingRatingApi(APIView):
    @csrf_exempt
    # get bookratings by sort highest to lowest 
    def book_list(request, pk=None):
        sort = Comment.objects.all().order_by('-score')
        if request.method == 'GET':
            serializer = BookSortingRatingSerializer(sort, many=True)
            return JsonResponse(serializer.data, status= 200, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = BookSortingRatingSerializer(data=data)
            #check if all fields are present
            if serializer.is_valid():
                #save the object to the db
                serializer.save()
                #display the new book comment, rating, and timestamp to the user
                return JsonResponse(serializer.data, status = 201)

class BookSorting():
    @csrf_exempt
    def all_genres(request):
        """client view to search for books associated with a specific genre"""
        Genre = Sorting.objects.all().order_by('Genre')
        return render(request, "Book_Genres.html", {'books': Genre})

    def all_ratings(request):
        """client view to search for books associated with a specific genre"""
        Rating = Sorting.objects.all().order_by('Rating')
        return render(request, "Book_Ratings.html", {'books': Rating})

    def all_top_sellers(request):
        """client view to search for books associated with a specific genre"""
        Copies_Sold = Sorting.objects.all().order_by('-Copies_Sold')
        return render(request, "Book_Top_Sellers.html", {'books': Copies_Sold})

class ApiListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSortingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination