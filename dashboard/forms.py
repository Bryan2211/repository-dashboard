from django import forms
from django.forms.extras.widgets import *

    
class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nom de la classe', max_length = 30)

class NewStudentForm(forms.Form):
    nickname = forms.CharField(label="Nom de l'élève", max_length=30)
    
class NewTeacherForm(forms.Form):
    nickname = forms.CharField(label="Nom du professeur", max_length=30)
    