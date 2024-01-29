from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # never change this code
    path('index', views.home, name="index"),
    path('contacts', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('login', views.user_login, name="login"),
    path('register', views.register, name="register"),
    path('admin', views.admin, name="admin-dash"),
    path('tnc', views.tnc, name="tnc"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user', views.user, name="user"),
    path('control', views.control, name="control"),
]
