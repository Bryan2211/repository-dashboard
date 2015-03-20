from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm, NewStudentForm, NewTeacherForm, AddHomeworkForm, SelectGroupForm, NewPasswordForm
from django.core.urlresolvers import reverse
from common.models import Group, Teacher, GroupMembers, Student, AssignHomework, Exercise, Quiz, Course
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
        userProfile = request.user
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            passwordConfirm = form.cleaned_data["passwordConfirm"]
            if password != passwordConfirm:
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
    homeworkExList = group.homeworkExercise.all()
    homeworkQuList = group.homeworkQuiz.all()
    homeworkCoList = group.homeworkCourse.all()

    deleteConfirmation = False
    
    if request.method == "POST":
        if 'addTeacher' in request.POST:
            erreurTeacher = False
            formTeacher = NewTeacherForm(request.POST)
            if formTeacher.is_valid():
                newTeacher = formTeacher.cleaned_data["nickname"]
                try:
                    try:
                        teacherUser = User.objects.get(username = newTeacher)
                        teacher = Teacher.objects.get(user = teacherUser)
                        newTeacherToGroup = GroupMembers(teacher = teacher, group = group)
                        newTeacherToGroup.save()
                    except User.DoesNotExist:
                        erreurTeacher = True
                except Teacher.DoesNotExist:
                    erreurTeacher = True
                    
                
        elif 'addStudent' in request.POST:
            formStudent = NewStudentForm(request.POST)
            erreurStudent = False
            if formStudent.is_valid():
                try:
                    try:
                        newStudent = formStudent.cleaned_data["nickname"]
                        studentUser = User.objects.get(username = newStudent)
                        student = Student.objects.get(user = studentUser)
                        newStudentToGroup = GroupMembers(student = student, group = group)
                        newStudentToGroup.save()
                    except User.DoesNotExist:
                        erreurStudent = True
                except Student.DoesNotExist:
                    erreurStudent = True
        elif 'assignHomework' in request.POST:
            formHomework = AddHomeworkForm(request.POST)
            erreur = False
            if formHomework.is_valid():
                homeworkid = formHomework.cleaned_data["homeworkid"]
                genre = formHomework.cleaned_data["genre"]
                
                if genre == "exercise":
                    try:
                        exercise = Exercise.objects.get(id = homeworkid)
                        newHomework = AssignHomework(exercise = exercise, group = group)
                        newHomework.save()
                    except Exercise.DoesNotExist:
                        erreur = True
                
                if genre == "quiz":
                    try:
                        quiz = Quiz.objects.get(id = homeworkid)
                        newHomework = AssignHomework(quiz = quiz, group = group)
                        newHomework.save()
                    except Quiz.DoesNotExist:
                        erreur = True
                
                if genre == "course":
                    try:
                        cours = Course.objects.get(id = homeworkid)
                        newHomework = AssignHomework(course = cours, group = group)
                        newHomework.save()
                    except Course.DoesNotExist:
                        erreur = True
        elif 'deleteClass' in request.POST:
            deleteConfirmation = True
        
        elif 'deleteClassConfirm' in request.POST:
            group = Group.objects.get(id = group_id)
            group.delete()
            return redirect('home')
            
        
        formStudent = NewStudentForm()
        formTeacher = NewTeacherForm()
        formHomework = AddHomeworkForm()
                    
    else:
        formStudent = NewStudentForm()
        formTeacher = NewTeacherForm()
        formHomework = AddHomeworkForm()
    return render(request, 'dashboard/templates/dashboard/classe.html', locals())
        
def deleteFromGroup(request, member_id, group_id):
    if request.method == "POST":
        if 'deleteStudent' in request.POST:
        
            student = Student.objects.get(id = member_id)
            group = Group.objects.get(id = group_id)
            studentToGroup = GroupMembers.objects.get(student = student, group = group)
            studentToGroup.delete()
            

        elif 'deleteTeacher' in request.POST:
            teacher = Teacher.objects.get(id = member_id)
            group = Group.objects.get(id = group_id)
            teacherToGroup = GroupMembers.objects.get(teacher = teacher, group = group)
            teacherToGroup.delete()
            
    return redirect('group_view', group_id = group_id)

def deleteActivity(request, activity_id):
    if request.method == "POST":
        if 'deleteExercise' in request.POST:
            exercise = Exercise.objects.get(id = activity_id)
            exercise.delete()
        if 'deleteQuiz' in request.POST:
            quiz = Quiz.objects.get(id = activity_id)
            quiz.delete()
        if 'deleteCourse' in request.POST:
            course = Course.objects.get(id = activity_id)
            course.delete()
    return redirect('exercises')
    
def deleteHomework(request, group_id, homework_id):
    if request.method == "POST":
        if 'deleteHomeworkEx' in request.POST:
            exercise = Exercise.objects.get(id = homework_id)
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.get(group = group, exercise = exercise)
            assignedHomework.delete()
        if 'deleteHomeworkQu' in request.POST:
            quiz = Quiz.objects.get(id = homework_id)
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.get(group = group, quiz = quiz)
            assignedHomework.delete()
        if 'deleteHomeworkCo' in request.POST:
            course = Course.objects.get(id = homework_id)
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.get(group = group, course = course)
            assignedHomework.delete()
    return redirect('group_view', group_id = group_id)
        
    
