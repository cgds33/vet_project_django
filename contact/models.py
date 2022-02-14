from tabnanny import verbose
from django.db import models
from phone_field import PhoneField

# Create your models here.


class Contact(models.Model):
    # Contact model fields
    # Contact model has defined for user's information
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Animal Lover")
    fullname = models.CharField(blank=True,max_length=50,verbose_name="Full Name")
    interest = models.CharField(blank=True,max_length=50,verbose_name="Interests")
    email = models.EmailField(blank=True,max_length=30,verbose_name="E-Mail")
    phone = PhoneField(blank=True,verbose_name="Phone Number")
    bio = models.TextField(blank=True,verbose_name="Biography")
    
    def __str__(self):
        return self.email


