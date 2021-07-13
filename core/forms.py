from django import forms
from django.forms import ModelForm
from .models import Vehiculo,Usuario
from django.core import validators


class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria','estado']

class User(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','email','password']        
