from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import models
from .models import booking



# Create your views here.

def cadmin(request):
    return render(request, 'admin/admin.html')

def login(request):
    return render(request, 'users/login.html')

def booking_index(request):
    if request.method == 'post':
        name = request.POST['name']
        destination = request.POST['destination']
        activity = request.POST['activity']
        date = request.POST['date']
        book = booking(name=name,activity=activity,destination=destination,date=date)
        book.save()
        return redirect('trip')
    return render(request, 'booking/booking_index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:

            if user.is_superuser:
                return redirect('cadmin')
            else:
                msg = "You are not autherized for this login"
                return render(request, 'users/login.html', {'msg': msg})
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'users/login.html', {'msg': msg})
    return render(request, 'users/login.html')
    

def trip(request):
    return render(request, 'booking/trip.html')
