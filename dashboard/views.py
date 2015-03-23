from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from dashboard.forms import NewGroupForm, NewStudentForm, NewTeacherForm, AddHomeworkForm, NewPasswordForm
from django.core.urlresolvers import reverse
from common.models import Group, Teacher, GroupMembers, Student, AssignHomework, Exercise, Quiz, Course
from django.contrib.auth.models import User
from django.http import HttpResponse

#Accueil du dashboard
def home(request):
    voyelle = 'aeiouyàäâéèëêîïíìôöõòûüùúAEIOUY' #Pour déterminer si le template affiche De ou D'
    user = Teacher.objects.get(user = request.user)
    firstLetter = request.user.username[0]#Idem
    return render(request, 'dashboard/templates/dashboard/index.html', locals())

#Exercices, quiz et cours
def exercises(request):
    user = Teacher.objects.get(user = request.user)
    return render(request, 'dashboard/templates/dashboard/exercises.html', locals())

#Création de groupe
def newgroup(request):
    success = False
    user = Teacher.objects.get(user = request.user)
    if request.method == "POST":
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data["group_name"]
            
            newGroup = Group.objects.create(name = group_name)
            newGroup.save()
            teacherToGroup = GroupMembers(teacher = user, group = newGroup) #Lie le Teacher et le groupe à travers la table intermédiaire
            teacherToGroup.save()
            success = True #Pour retourner le message de confirmation
    else:
        form = NewGroupForm()
    return render(request, "dashboard/templates/dashboard/newclass.html", locals())

#Changement de mot de passe
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
                success = False #Message d'erreur
            else:
                success = True #Message de confirmation
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
    homeworkExList = group.homeworkExercise.all()#
    homeworkQuList = group.homeworkQuiz.all()    # Pour avoir la liste des devoirs selon les genres d'activités
    homeworkCoList = group.homeworkCourse.all()  #

    deleteConfirmation = False #Pour supprimer une classe
    
    if request.method == "POST":
        
        #Ajouter un professeur au groupe
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
                        erreurTeacher = True #Message d'erreur
                except Teacher.DoesNotExist:
                    erreurTeacher = True #Idem
                    
        #Ajouter un élève au groupe       
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
                        erreurStudent = True #Message d'erreur
                except Student.DoesNotExist:
                    erreurStudent = True #Idem
                    
                    
        #Assigner un devoir
        elif 'assignHomework' in request.POST:
            formHomework = AddHomeworkForm(request.POST)
            erreur = False
            if formHomework.is_valid():
                homeworkid = formHomework.cleaned_data["homeworkid"]
                genre = formHomework.cleaned_data["genre"]
                
                #Cherche l'activité selon le genre choisi
                if genre == "exercise":
                    try:
                        exercise = Exercise.objects.get(id = homeworkid)
                        newHomework = AssignHomework(exercise = exercise, group = group)
                        newHomework.save()
                    except Exercise.DoesNotExist:
                        erreur = True #Message d'erreur
                
                if genre == "quiz":
                    try:
                        quiz = Quiz.objects.get(id = homeworkid)
                        newHomework = AssignHomework(quiz = quiz, group = group)
                        newHomework.save()
                    except Quiz.DoesNotExist:
                        erreur = True #Idem
                
                if genre == "course":
                    try:
                        cours = Course.objects.get(id = homeworkid)
                        newHomework = AssignHomework(course = cours, group = group)
                        newHomework.save()
                    except Course.DoesNotExist:
                        erreur = True #Idem
        elif 'deleteClass' in request.POST:
            deleteConfirmation = True #Fait apparaître le deuxième bouton de confirmation
        
        #Supprime la classe
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

#Retirer d'un groupe
def deleteFromGroup(request, member_id, group_id):
    if request.method == "POST":
        
        #Selon élève ou professeur
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

#Supprimer une activité
def deleteActivity(request, activity_id):
    if request.method == "POST":
        
        #Selon exercice, quiz ou cours
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

#Retirer un devoir   
def deleteHomework(request, group_id, homework_id):
    if request.method == "POST":
        
        #Selon exercice, quiz ou cours
        if 'deleteHomeworkEx' in request.POST:
            exercise = Exercise.objects.filter(id = homework_id)
            exercise = exercise[0]
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.filter(group = group, exercise = exercise)
            assignedHomework = assignedHomework[0]
            assignedHomework.delete()
        if 'deleteHomeworkQu' in request.POST:
            quiz = Quiz.objects.filter(id = homework_id)
            quiz = quiz[0]
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.filter(group = group, quiz = quiz)
            assignedHomework = assignedHomework[0]
            assignedHomework.delete()
        if 'deleteHomeworkCo' in request.POST:
            course = Course.objects.filter(id = homework_id)
            course = course[0]
            group = Group.objects.get(id = group_id)
            assignedHomework = AssignHomework.objects.filter(group = group, course = course)
            assignedHomework = assignedHomework[0]
            assignedHomework.delete()
    return redirect('group_view', group_id = group_id)