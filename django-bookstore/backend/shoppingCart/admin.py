from django.contrib import admin
from shoppingCart.models import Cart

class shoppingCartAdmin(admin.ModelAdmin):
    list_display = ('books')



admin.site.register(Cart)
