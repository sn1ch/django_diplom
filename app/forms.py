from django import forms
from .models import User


class CartAddProductForm(forms.Form):
    pass


class UserAuthenticationForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ['email', 'password']
