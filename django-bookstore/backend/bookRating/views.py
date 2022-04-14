from django.db.models import Avg
from bookRating.models import Comment
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from bookRating.serializers import CommentSerializer, CommentAverageSerializer
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class CommentView(APIView):
    @csrf_exempt
    # get bookratings by sort highest to lowest 
    def comments(request, pk=None):
        comment = Comment.objects.all().order_by('-score')
        if request.method == 'GET':
            serializer = CommentSerializer(comment, many=True)
            return JsonResponse(serializer.data, status= 200, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CommentSerializer(data=data)
            #check if all fields are present
            if serializer.is_valid():
                #save the object to the db
                serializer.save()
                #display the new book comment, rating, and timestamp to the user
                return JsonResponse(serializer.data, status = 201)




class Average(ListModelMixin, GenericAPIView): 
    serializer_class = CommentAverageSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Comment.objects.all().annotate(Avg('score'))
