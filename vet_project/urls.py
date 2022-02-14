"""vet_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pets import views

from django.conf import settings
from django.conf.urls.static import static

# Project's URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('objectives/', views.objectives,name="objectives"),
    path('pets/',include("pets.urls")), # Redirect to pets's urls.py
    path('user/',include("user.urls")), # Redirect to user's urls.py
    path('profile/',include("contact.urls")), # Redirect to contact's urls.py
]

# For static media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

