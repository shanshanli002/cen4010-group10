from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("rating", "userz", "book", "date") # include "publish" for extra display 
    list_filter = ("date") # for filtering the comment by approval and date 
    search_fields = ("userz", "body", "rating")


admin.site.register(Comments,CommentAdmin)