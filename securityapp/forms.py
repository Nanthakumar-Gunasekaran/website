from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput)
