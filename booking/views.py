from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import booking
from django.contrib.auth.decorators import login_required



# Create your views here.

def cadmin(request):
    return render(request, 'admin/admin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:

            if user.is_superuser:
                return redirect('cadmin')
            elif user.is_user:
                return redirect('booking_index')
            else:
                msg = "You are not autherized for this login"
                return render(request, 'users/login.html', {'msg': msg})
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'users/login.html', {'msg': msg})
    return render(request, 'users/login.html')


@login_required(login_url='login')
def booking_index(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        destination = request.POST['destination']
        activity = request.POST['activity']
        date = request.POST['date']
        book = booking.objects.create(name=name,activity=activity,destination=destination,date=date)
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
            elif user.is_user:
                return redirect('booking_index')
            else:
                msg = "You are not autherized for this login"
                return render(request, 'users/login.html', {'msg': msg})
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'users/login.html', {'msg': msg})
    return render(request, 'users/login.html')

def trip(request):
    return render(request, 'booking/trip.html')


