from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm, NewStudentForm, NewTeacherForm, AddHomeworkForm, SelectGroupForm
from django.core.urlresolvers import reverse
from common.models import Group, Teacher, GroupMembers
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    user = request.user
    return render_to_response('dashboard/templates/dashboard/index.html', locals())

def group(request, numGroup):
    #group = get_object_or_404(Group, numGroup)
    if request.method == "POST":
        formStudent = NewStudentForm(request.POST)
        if formStudent.is_valid:
            newStudent = formStudent.cleaned_data["newStudent"]
            Group.student.add(newStudent)
            Group.save()
        formTeacher = NewTeacherForm(request.POST)
        if formTeacher.is_valid:
            newTeacher = formStudent.cleaned_data["newTeacher"]
            Group.teacher.add(newTeacher)
            Group.save()
    return render(request, 'dashboard/templates/dashboard/classe.html', locals())

def exercises(request):
    return render_to_response('dashboard/templates/dashboard/exercises.html')
    
def newgroup(request):
    user = Teacher.objects.get(id = request.user.id)
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["group_name"]
            
            newGroup = Group.objects.create(name = group_name)
            newGroup.save()
            teacherToGroup = GroupMembers(teacher = user, group = newGroup)
            teacherToGroup.save()
            return HttpResponse("Classe correctement créée")
    return render(request, "dashboard/templates/dashboard/newclass.html", locals())
    
def manage(request):
    
    return render(request, "dashboard/templates/dashboard/manage.html", locals())
    
        
