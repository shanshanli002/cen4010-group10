from django.contrib import admin
from .models import Cart

class shoppingCartAdmin(admin.ModelAdmin):
    list_display = ('books')



admin.site.register(Cart, shoppingCartAdmin)
