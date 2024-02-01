from django.urls import path
from . import views

urlpatterns = [
    path('trip',views.trip, name = "trip"),
    path('booking_index',views.booking_index, name = "booking_index"),
]