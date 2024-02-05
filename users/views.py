from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models
from .models import blog, feedback
from datetime import datetime, timedelta
from booking.models import booking





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
                return redirect('cadmin')
            else:
                login(request,user)
                return redirect('index')  
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'users/login.html', {'msg': msg})
    return render(request, 'users/login.html')
        
def user_logout(request):
    logout(request)
    return redirect('user_login')

def index(request):
    return render(request, 'users/index.html')

@login_required(login_url='user_login')
def form(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        message = request.POST['message']
        blg = blog.objects.create(username=username, email=email, message=message)
        blg.save()
        return render(request, 'users/form.html') 
    return render(request, 'users/form.html')


def home(request):
    return render(request, 'users/index.html')


def control(request):
    Blog = blog.objects.all()
    return render(request, 'admin/control.html', {'blog':Blog})


def user(request):
    register = User.objects.all()
    return render(request, 'admin/user.html',{'register':register})

def trip(request):
    return render(request, 'booking/trip.html')

def contact(request):
    cntct = feedback.objects.all()
    return render(request, 'users/contacts.html',{'feedback':cntct})


def Blog(request):
    blg = blog.objects.all()
    return render(request, 'users/blog.html', {'blog':blg})


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

def deleteusr(request,id):
    delete = User.objects.get(id=id)
    delete.delete()
    return redirect('user')

# def editusr(request,id):
#     edit = User.objects.get(id=id)
#     edit.edit()
#     return redirect('user')


def tnc(request):
    return render(request, 'users/tnc.html')


# def userData(request):
#     context={

#     }
#     return render(request, "users/UserData.html",context)
# return render(request, 'users/register.html')

 


def dashboard(request):
    bkng = booking.objects.all()
    return render(request, 'admin/admin.html', {'bkng' : bkng })

def show_total_blogs(request):
    total_blogs = blog.objects.count()
    return render(request, 'admin.html', {'total_blogs': total_blogs})

def total_users(request):
    total_users = User.objects.count()
    return render(request, 'admin.html', {'total_users': total_users})

def new_users(request):
    one_week_ago = datetime.now() - timedelta(days=7)
    new_users_count = User.objects.filter(date_joined__gte=one_week_ago).count()

    return render(request, 'admin/admin.html', {'new_users_count': new_users_count})