from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# from .models import userDetails


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
        


def index(request):
    return render(request, 'users/index.html')


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
    errors = {}
    if request.method == 'POST':

        name = request.POST['name'].strip()

        email = request.POST['email'].strip()

        password = request.POST['pass'].strip()
        password = request.POST['pass'].strip()

        new_user = User.objects.create_user(username=name, email=email)
        new_user.set_password('pass')
        new_user.save()
        # userDetails.objects.create(user=new_user,)
        return redirect('login')
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
