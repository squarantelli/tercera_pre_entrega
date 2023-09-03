from django import forms

class formSetCliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class formSetRemera(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    talle = forms.CharField(max_length=3)

class formSetTaza(forms.Form):
    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)