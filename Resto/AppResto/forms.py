from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *


class BebidaFormulario(forms.Form):
    bebida = forms.CharField()
    precio = forms.IntegerField()

class platoFormulario(forms.Form):
    plato = forms.CharField()
    precio = forms.IntegerField()  

class postreFormulario(forms.Form):
    postre = forms.CharField()
    precio = forms.IntegerField()   

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password2(self):
        print('self\n', self.cleaned_data)
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no son iguales!")
        return password2

class UserRegisterForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')