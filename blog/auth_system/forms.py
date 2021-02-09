from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class RegistrationForm(UserCreationForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ("username","email","password1","password2")


class UserUpdaterForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ("username","email")


class ProfileUpdaterForm(forms.ModelForm):  
  class Meta:
    model = profile
    fields = ("img",)