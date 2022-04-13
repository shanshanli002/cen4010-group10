from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from bookRating.models import Comment
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book
from bookRating.forms import CommentForm

class CommentView():

    def comment_Rating(request):
        if request.method == 'GET':
            sorted = Comment.objects.all()
            return render(request, "Comment_Rating.html", {'sorted': sorted}) 

    def comment_Average(request):
        if request.method == 'GET':
            average = Comment.objects.all().aggregate(Avg('score'))
            return HttpResponse(average)



"""
    def product_page(request, pk):
        book = get_object_or_404(Book, pk=pk)

        if not request.user.is_authenticated:
            is_comment_allowed = False
        else:
            is_comment_allowed = (
                not request.user.comments.filter(book__pk=pk).exists()
                and book in request.user.books.all()
            )
        
        if request.method == "GET" or not is_comment_allowed:
            return render(
                request, "product.html",
                dict(book=book, is_comment_allowed=is_comment_allowed)
            )

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.author = request.user
            comment.save()
            if book.score == 0:
                book.score = comment.score
            else:
                book.score = (book.score + comment.score) / 2.0
            book.save()
        
        return redirect("product_page", pk=pk)
"""