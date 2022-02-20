from django.contrib import admin

# Register your models here.
from.models import *


class Customer(admin.ModelAdmin):
    model = Customer
    
class Product(admin.ModelAdmin):
    model = Product
    
class Tag(admin.ModelAdmin):
    model = Tag
    
class Order(admin.ModelAdmin):
    model = Order    
    
    
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
