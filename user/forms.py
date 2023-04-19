from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email Address'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter User Name'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Your Password'}), label='Password')
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': ' Confirm Your Password'}), label='Password Confirmation')

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
