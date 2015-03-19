from django import forms
from django.forms.extras.widgets import *

    
class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nom du groupe', max_length = 30)

class NewStudentForm(forms.Form):
    nickname = forms.CharField(label="Nom de l'élève", max_length=30)
    
class NewTeacherForm(forms.Form):
    nickname = forms.CharField(label="Nom du professeur", max_length=30)
    
class AddHomeworkForm(forms.Form):
    homeworkid = forms.CharField(label="Id de l'exercice", max_length=30)
    genre = forms.ChoiceField(label="Type de devoir", choices =(
        ("exercise", "Exercice"),
        ("quiz", "Quiz"),
        ("course", "Cours"),
        ))
    
class SelectGroupForm(forms.Form):
    group_name = forms.CharField(label='Nom de la classe', max_length = 30)
    
class NewPasswordForm(forms.Form):
    currentPassword = forms.CharField(label='Mot de passe actuelle', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    passwordConfirm = forms.CharField(label='Confirmation du nouveau mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    