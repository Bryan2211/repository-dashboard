from django import forms
from django.forms.extras.widgets import *

#Pour créer un groupe
class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nom du groupe', max_length = 30)

#Pour ajouter un student à un groupe
class NewStudentForm(forms.Form):
    nickname = forms.CharField(label="Nom de l'élève", max_length=30)

#Pour ajouter un teacher à un groupe
class NewTeacherForm(forms.Form):
    nickname = forms.CharField(label="Nom du professeur", max_length=30)

#Pour assigner un devoir à un groupe   
class AddHomeworkForm(forms.Form):
    homeworkid = forms.CharField(label="Numéro de l'exercice", max_length=30)
    #Choisir selon le type d'activité
    genre = forms.ChoiceField(label="Type de devoir", choices =(
        ("exercise", "Exercice"),
        ("quiz", "Quiz"),
        ("course", "Cours"),
        ))
#Changement de mot de passe
class NewPasswordForm(forms.Form):
    password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    passwordConfirm = forms.CharField(label='Confirmation du nouveau mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    