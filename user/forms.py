from django import forms
from django.contrib.auth.models import User
from .models import Profile, Address
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter First Name'}), required=False)
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Last Name'}), required=False)
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


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)
    email = forms.EmailField(label='Email', required=False)
    username = forms.CharField(label='Username', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class profileUpdateForm(forms.ModelForm):
    phone = forms.CharField(label='Phone', required=False)
    image = forms.ImageField(label='Upload Image',
                             widget=forms.FileInput(
                                 attrs={
                                     "style": "height: 35px ; width : 100% ; "}
                             )
                             )

    class Meta:
        model = Profile
        fields = ['phone', 'image']


class profileAddressUpdateForm(forms.ModelForm):
    city = forms.CharField(label='City', required=False)
    state = forms.CharField(label='State', required=False)
    country = forms.CharField(label='Country', required=False)
    house_no = forms.CharField(label='Address', required=False)

    class Meta:
        model = Address
        fields = ['city', 'state', 'country', 'house_no']
