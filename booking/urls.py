from django.urls import path
from . import views

urlpatterns = [
    path('user_login',views.user_login, name = "user_login"), 
    path('booking_index',views.booking_index, name = "booking_index"), 
    path('trip',views.trip, name = "trip"),
]