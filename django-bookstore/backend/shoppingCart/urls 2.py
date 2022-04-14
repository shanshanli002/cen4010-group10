from django.urls import include, path
from .views import CartView

urlpatterns = [
    path("shoppingCart/add/", CartView.addToCart, name = "shoppingCart_add"),
    path("shoppingCart/remove/", CartView.removeFromCart, name = "shoppingCart_remove"),
    path("shoppingCart/submit/", CartView.createCart, name = "shoppingCart_submit"),
    path("shoppingCart/viewAll/", CartView.as_view, name = "shoppingCart_viewAll/")
]