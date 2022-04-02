
"""from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from .forms import CommentForm


def index(request):
    return HttpResponse("test")

# Create your views here.
#---------------------------------------------------------------------------------------------
@login_required(login_url='login') #user is able to access book details only 
def book_detail_view(request, book_id): #for book details or example of one 

    books = get_object_or_404(Books, pk=book_id)

    context = {'books': books,}

    return render(request, 'book_detail.html', context)

@login_required(login_url='login') #user is able to access comments only 
def add_comment(request, comment_id):

    form = CommentForm() # form - format of comment saved 
    books = get_object_or_404(Books, pk=comment_id) # collect information from the book
    user = request.user #user must be created 

    # if someone has made a comment checking and monitoring 
    if request.method == "POST": 
        form = CommentForm(request.POST) # collect information from request data to comment_form
        if form.is_valid(): # checking information is valid 
            comment = form.save(commit=False) # preparing to save data but not yet commited 
            comment.user = user # saving user information
            comment.book = books # saving book information
            comment.save() # saving to database
            return redirect('book_detail', books.id) # redirect to the page of the book

    context = {'form': form}

    return render(request, 'comment_form.html', context) # need to create front end html 
#---------------------------------------------------------------------------------------------



#def post_single(request, post): # refers to page where book is SO remove "post_single" and include the comment field as an extension to a book "post" is also a model 

#    post = get_object_or_404(Post, slug=post, status='publised') # switch slug and collect information from the post

#    comments = post.comments.filter(status=True) # get comment that are true 

#    user_comment = None

#    # if someone has made a comment checking and monitoring 
#    if request.method == 'POST': 
#        comment_form = NewCommentForm(request.POST) # collect information from post data to comment_form
#        if comment_form.is_valid(): # checking information is valid 
#            user_comment = comment_form.save(commit=False) # preparing to save data but not yet commited 
#            user_comment.post = post # saving post information
#            user_comment.save() # saving to database 
#            return HttpsResponseRedirect( '/' + post.slug) # change slug redirect to page of comment that was submitted 
#                                                           # slug rerfers to post 
#        else: #return to where the comment are found I think 
#            comment_form = NewCommentForm()
#        return render(
#            request, "single.html",
#            {
#                'post': post,
#                'comments': user_comment,
#                'comments': comments,
#                'comment_form': comment_form
#            },
#        )

"""