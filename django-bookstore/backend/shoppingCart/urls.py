from django.urls import include, path
from . import views

urlpatterns = [
    path("shoppingCart/add/", views.addToCart, name = "shoppingCart_add"),
    path("shoppingCart/remove/", views.removeFromCart, name = "shoppingCart_remove"),
    path("shoppingCart/submit/", views.submitCart, name = "shoppingCart_submit"),
    path("shoppingCart/viewAll/", views.all_items, name = "shoppingCart_viewAll/")
]