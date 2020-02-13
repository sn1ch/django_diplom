from django import forms
from .models import User


class UserAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(object):
        model = User
        fields = ['email', 'password']
    #     # exclude = ('id', 'product')
