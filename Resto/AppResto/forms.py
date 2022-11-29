from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class BebidaFormulario(forms.Form):
    bebida = forms.CharField()
    precio = forms.IntegerField()

class UserEditForm(UserChangeForm):
    class meta:
        model = User
        fields = ['email', 'first_name', 'last name']