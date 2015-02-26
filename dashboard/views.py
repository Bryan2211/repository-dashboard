from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm
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
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["group_name"]
            teacher = user
            group = Group.objects.create_group(name, teacher)
            group.save()
            return HttpResponse("Classe corrrectement créée")
    return render(request, "dashboard/templates/dashboard/newclass.html", locals())
