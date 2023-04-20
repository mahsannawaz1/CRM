from django import forms
from django.contrib.auth.models import User
from .models import Product, Order


class productCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=255, label='Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Name'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Description'}))
    price = forms.DecimalField(decimal_places=2, max_digits=6, label='Price', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Price'}))
    weight = forms.DecimalField(
        decimal_places=2, max_digits=6, label='Weight (in LBS)', widget=forms.TextInput(
            attrs={'placeholder': 'Enter Product Weight'}))
    barcode = forms.CharField(max_length=12, label='BarCode', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Product Barcode'}))
    inventory = forms.IntegerField(min_value=0, label='Inventory', widget=forms.TextInput(
        attrs={'placeholder': "Enter Product's Inventory"}))
    image = forms.ImageField(label='Upload Image',
                             widget=forms.FileInput(
                                 attrs={
                                     "style": "height: 35px ; width : 100% ; "}
                             ), required=False
                             )

    class Meta:
        model = Product
        fields = '__all__'
