from django import forms
from django.forms.extras.widgets import *

    
class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nom de la classe', max_length = 30)
    