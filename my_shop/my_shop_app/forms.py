from django import forms
from .models import Order,User_register,User_login

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'category', 'products', 'phone']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User_login
        fields = ['Username', 'Password']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User_register
        fields = ['Username', 'Password', 'phone']