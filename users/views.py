from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import models



# from .models import userDetails


def user_login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        print(username1, password1)
        user = authenticate(request, username=username1, password=password1)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return render('cadmin')
            else:
                login(request,user)
                return render('index')  
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'users/login.html', {'msg': msg})
    return render(request, 'users/login.html')
        


def index(request):
    return render(request, 'users/index.html')

@login_required(login_url='user_login')
def form(request):
    return render(request, 'users/form.html')


def home(request):
    return render(request, 'users/index.html')


def control(request):
    return render(request, 'admin/control.html')


def user(request):
    return render(request, 'admin/user.html')

def trip(request):
    return render(request, 'booking/trip.html')

def contact(request):
    return render(request, 'users/contacts.html')


def blog(request):
    return render(request, 'users/blog.html')


def register(request):
    return render(request, 'users/register.html')


def cadmin(request):
    return render(request, 'admin/admin.html')



def register(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        email = request.POST['email'].strip()
        password = request.POST['pass'].strip()

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        # userDetails.objects.create(user=new_user,)
        return redirect('user_login')
    else:
        return render(request, 'users/register.html')


def tnc(request):
    return render(request, 'users/tnc.html')


# def userData(request):
#     context={

#     }
#     return render(request, "users/UserData.html",context)
# return render(request, 'users/register.html')
def dashboard(request):
    return render(request, 'admin/admin.html')
