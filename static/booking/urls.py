from django.urls import path
from . import views

urlpatterns = [
    path('user_login',views.user_login, name = "user_login"),  
    path('trip',views.trip, name = "trip"),
    path('booking_index',views.booking_index, name = "booking_index"),
]