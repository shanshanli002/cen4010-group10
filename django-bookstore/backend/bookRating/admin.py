from django.contrib import admin
from .models import *

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "body","rating","date") 
    #list_filter = ("date","body") # for filtering the comment by approval and date 
    #search_fields = ("users", "body", "rating")


admin.site.register(Comment,CommentAdmin)