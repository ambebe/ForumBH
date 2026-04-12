from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar"]
