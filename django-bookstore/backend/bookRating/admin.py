from django.contrib import admin
from . import models #added import 

# Register your models here.

"""""
@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("rating", "user", "book") # include "publish" for extra display 
    list_filter = ("date") # for filtering the comment by approval and date 
    search_fields = ("user", "body", "rating")
"""