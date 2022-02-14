from django.contrib import admin
from django.urls import path
from . import views

# Defines the app name
app_name = "contact"

# Contact app's URL patterns
urlpatterns = [
    path('', views.profile, name="profile"),
    path('contact/', views.contact, name="contact"),
    path('author/<int:id>', views.sProfile, name="sprofile"),
]

