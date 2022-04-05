from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from books.models import Book
from users.models import Users
from django.contrib.auth.decorators import login_required


#@login_required(login_url='login')
def add_comment(request, comment_id):

    #form = CommentForm() # form - format of comment saved 
    books = get_object_or_404(Book, pk=comment_id) # collect information from the book
    user = request.Users #user must be created 

    # if someone has made a comment checking and monitoring 
    if request.method == "POST": 
        form = request.POST # collect information from request data to comment_form
        if form.is_valid(): # checking information is valid 
            comment = form.save(commit=False) # preparing to save data but not yet commited 
            comment.user = user # saving user information
            comment.book = books # saving book information
            comment.save() # saving to database
            return redirect('book_detail', books.id) # redirect to the page of the book

    context = {'form': form}

    return render(request, 'comment_form.html', context) # need to create front end html 

#---------------------------------------------------------------------------------------------
