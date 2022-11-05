from django import forms

class BebidaFormulario(forms.Form):
    codBebida = forms.IntegerField()
    bebida = forms.CharField()
    precio = forms.IntegerField()

class PostreFormulario(forms.Form):
    codPostre = forms.IntegerField()
    postre = forms.CharField()
    precio = forms.IntegerField()

class PlatoPpalFormulario(forms.Form):
    combo = forms.IntegerField()
    plato = forms.CharField()
    guarnicion = forms.CharField()
    precio = forms.IntegerField()