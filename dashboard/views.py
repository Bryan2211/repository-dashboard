from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import LoginForm, NewGroupForm
from django.core.urlresolvers import reverse
from dashboard.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render_to_response('dashboard/templates/dashboard/index.html')

def group(request):
    return render_to_response('dashboard/templates/dashboard/class.html')

def exercises(request):
    return render_to_response('dashboard/templates/dashboard/exercises.html')
    
def newgroup(request):
    return render_to_response('dashboard/templates/dashboard/newclass.html')
    
def connexion(request):
    erreur = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                erreur = True
    else:
        form = LoginForm()
        
    return render(request, "dashboard/templates/dashboard/login.html", locals())
