from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm, NewStudentForm, NewTeacherForm
from django.core.urlresolvers import reverse
from common.models import Group, Teacher
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render_to_response('dashboard/templates/dashboard/index.html')

def group(request):
    if request.method == "POST":
        formStudent = NewStudentForm(request.POST)
        if formStudent.is_valid:
            newStudent = formStudent.cleaned_data["newStudent"]
            Group.student.add(newStudent)
            Group.save()
        formTeacher = NewTeacherForm(request.POST)
        if formTeacher.is_valid:
            newTeacher = formTeacher.cleaned_data["newTeacher"]
            Group.teacher.add(newTeacher)
            Group.save()
    return render_to_response('dashboard/templates/dashboard/class.html')

def exercises(request):
    return render_to_response('dashboard/templates/dashboard/exercises.html')
    
def newgroup(request):
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["group_name"]
            
            group = Group(name = group_name)
            group.save()
            group.teacher = Teacher
            group.save()
            return HttpResponse("Classe corrrectement créée")
    return render(request, "dashboard/templates/dashboard/newclass.html", locals())
    
        
