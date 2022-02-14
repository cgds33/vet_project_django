from django.contrib import admin
from django.urls import path
from . import views

# Defines the app name
app_name = "pets"

# Pet app's URL patterns
urlpatterns = [
    path('dasboard/', views.dashboard, name="dashboard"),
    path('addpet/', views.addpet, name="addpet"),
    path('pet/<int:id>', views.detail, name="detail"),
    path('allpets/', views.allPets, name="allpets"),
    path('update/<int:id>', views.updatePet, name="update"),
    path('delete/<int:id>', views.deletePet, name="delete"),
]


