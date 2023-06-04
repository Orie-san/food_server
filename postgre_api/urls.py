from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.authenticate_user),
]
