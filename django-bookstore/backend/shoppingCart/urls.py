from django.urls import include, path
from rest_framework import routers
from shoppingCart import views

router = routers.DefaultRouter()
router.register(r'cart', views.CartView)
router.register(r'user', views.UserView)

urlpatterns = [
    path('', include((router.urls, 'django-bookstore.backend.shoppingCart'))),
]