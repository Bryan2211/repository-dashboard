from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm, NewStudentForm, NewTeacherForm, AddHomeworkForm, SelectGroupForm, NewPasswordForm
from django.core.urlresolvers import reverse
from common.models import Group, Teacher, GroupMembers, Student
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    voyelle = 'aeiouyàäâéèëêîïíìôöõòûüùúAEIOUY'
    user = Teacher.objects.get(user = request.user)
    firstLetter = request.user.username[0]
    return render(request, 'dashboard/templates/dashboard/index.html', locals())

def exercises(request):
    user = Teacher.objects.get(user = request.user)
    return render(request, 'dashboard/templates/dashboard/exercises.html', locals())
    
def newgroup(request):
    success = False
    user = Teacher.objects.get(user = request.user)
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["group_name"]
            
            newGroup = Group.objects.create(name = group_name)
            newGroup.save()
            teacherToGroup = GroupMembers(teacher = user, group = newGroup)
            teacherToGroup.save()
            success = True
    else:
        form = NewGroupForm()
    return render(request, "dashboard/templates/dashboard/newclass.html", locals())
    
def manage(request):
    user = Teacher.objects.get(user = request.user)
    return render(request, "dashboard/templates/dashboard/manage.html", locals())
    
def profil(request):
    user = Teacher.objects.get(user = request.user)
    success = ''
    if request.method == "POST":
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            currentPassword = form.cleaned_data["currentPassword"]
            password = form.cleaned_data["password"]
            passwordConfirm = form.cleaned_data["passwordConfirm"]
            if password != passwordConfirm or currentPassword != request.user.password:
                success = False
            else:
                success = True
                u = request.user
                u.set_password(password)
                u.save()
    else:
        form = NewPasswordForm()
    return render(request, 'dashboard/templates/dashboard/profile.html', locals())
    
def group(request, group_id):
    user = Teacher.objects.get(user = request.user)
    group = Group.objects.get(id = group_id)
    studentList = group.student.all()
    teacherList = group.teacher.all()
    
    if request.method == "POST":
        if 'addTeacher' in request.POST:
            formTeacher = NewTeacherForm(request.POST)
            if formTeacher.is_valid():
                newTeacher = formTeacher.cleaned_data["nickname"]
                teacherUser = User.objects.get(username = newTeacher)
                teacher = Teacher.objects.get(user = teacherUser)
                newTeacherToGroup = GroupMembers(teacher = teacher, group = group)
                newTeacherToGroup.save()
        elif 'addStudent' in request.POST:
            formStudent = NewStudentForm(request.POST)
            if formStudent.is_valid():
                newStudent = formStudent.cleaned_data["nickname"]
                studentUser = User.objects.get(username = newStudent)
                student = Student.objects.get(user = studentUser)
                newStudentToGroup = GroupMembers(student = student, group = group)
                newStudentToGroup.save()
    else:
        formStudent = NewStudentForm()
        formTeacher = NewTeacherForm()
        formHomework = AddHomeworkForm()
    return render(request, 'dashboard/templates/dashboard/classe.html', locals())
    
def addTeacher(request):
    if request.method == "POST":
        formTeacher = NewTeacherForm(request.POST)
        if formTeacher.is_valid():
            newTeacher = formTeacher.cleaned_data["nickname"]
            teacherUser = User.objects.get(username = newTeacher)
            teacher = Teacher.objects.get(user = teacherUser)
            newTeacherToGroup = GroupMembers(teacher = teacher, group = group)
            newTeacherToGroup.save()
            
def addStudent(request):
    if request.method == "POST":
        formStudent = NewStudentForm(request.POST)
        if formStudent.is_valid():
            newStudent = formStudent.cleaned_data["nickname"]
            studentUser = User.objects.get(username = newStudent)
            student = Student.objects.get(user = studentUser)
            newStudentToGroup = GroupMembers(student = student, group = group)
            newStudentToGroup.save()
    
        
