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

class CommentView(APIView):

    # get bookratings by sort highest to lowest 
    def get(request, pk=None):
        comment = Comment.objects.all().order_by('-score')
        if request.method == 'GET':
            serializer = CommentSerializer(comment, many=True)
        return JsonResponse(serializer.data, status= 200, safe=False)


class Average(ListModelMixin, GenericAPIView): 
    serializer_class = CommentAverageSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):

        return Comment.objects.all().annotate(Avg('score'))
