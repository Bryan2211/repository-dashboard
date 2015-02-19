from django import forms
from django.forms.extras.widgets import *


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class NewGroupForm(forms.Form):
    name = forms.CharField(label='Nom de la classe', max_length = 30)
    student = forms.CharField(label="Pseudo de l'élève", max_length = 30)

    