from django.urls import path
#from . import views
#from django.contrib.auth import views as auth_view
#from django.conf.urls import url 
#from payments import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path


urlpatterns = [
    #path('', views.home, name='home'),
    #path('register/', views.register, name='register'),
    #path('profile/', views.profile, name='profile'),
    #path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    #path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    #url(r'^test-payment/$', views.test_payment),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
