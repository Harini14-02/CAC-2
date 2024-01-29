from django.urls import path
from . import views

urlpatterns = [
    path('trip', views.trip, name = "trip"),
    path('login',views.login, name = "login"), 
]