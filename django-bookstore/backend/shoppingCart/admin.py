from django.contrib import admin

class shoppingCartAdmin(admin.ModelAdmin):
    list_display = ('books')



admin.site.register(shoppingCartAdmin)
