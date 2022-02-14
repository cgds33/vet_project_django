from django import forms
from .models import Pet

# Defining the Pet form fields
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["petName","petType","petSpecies","petAge","content","petImage"]

