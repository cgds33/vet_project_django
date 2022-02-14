from django import forms
from .models import Contact

# Defining the Contact form fields
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["fullname","email","interest","phone","bio"]



