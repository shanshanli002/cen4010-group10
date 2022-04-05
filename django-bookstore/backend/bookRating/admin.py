from django.contrib import admin
from bookRating.models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ("rating", "user", "book", "date") # include "publish" for extra display 
    list_filter = ("date","body") # for filtering the comment by approval and date 
    search_fields = ("users", "body", "rating")


admin.site.register(Comment,CommentAdmin)