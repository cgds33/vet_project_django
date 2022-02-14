from django.contrib import admin
from django.urls import path
from . import views

# Defines the app name
app_name = "user"

# User app's URL patterns
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('users/', views.allUsers, name="allusers"),
]
