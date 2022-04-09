from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from bookRating.models import Comment
from django.http import HttpResponse

class CommentView():

    def comment_Rating(request):
        sorted = Comment.objects.all().order_by('-score')
        return HttpResponse(sorted)

    def comment_Average(request):
        average = Comment.objects.all().aggregate(Avg('score'))
        return HttpResponse(average)

