from django.shortcuts import render

# Create your views here.
def trip(request):
    return render(request, 'booking/trip.html')

def login(request):
    return render(request, 'booking/login.html')