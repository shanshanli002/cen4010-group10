from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='bookRating'),
#---------------------------------------------------------------------------------------------
    # BOOKS
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),

    # COMMENTS
    path('book/<int:comment_id>/comment/', views.add_comment, name='add_comment'),
#---------------------------------------------------------------------------------------------
]