from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # never change this code
    path('index', views.home, name="home"),
    path('contacts', views.contact, name="contact"),
    path('Blog', views.Blog, name="Blog"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('register', views.register, name="register"),
    path('cadmin', views.cadmin, name="cadmin"),
    path('tnc', views.tnc, name="tnc"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user', views.user, name="user"),
    path('form', views.form, name="form"),
    path('control', views.control, name="control"),
]
