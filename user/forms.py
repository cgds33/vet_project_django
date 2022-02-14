from django import forms
from django.contrib.auth.models import User

# Login form class
class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Parola", widget=forms.PasswordInput)
    # Django has a "Clean" method for this form although we don't see it 

# Register form class
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,label="Username")
    password = forms.CharField(max_length=20,label="Password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Confirm Password",widget=forms.PasswordInput)

    # Built based on django recommendations 
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm):
            raise forms.ValidationError("Passwords did not match!")
        if User.objects.filter(username = username).first():
            raise forms.ValidationError("This username is already taken!")
        
        values = {
            "username": username,
            "password": password
        }
        return values




