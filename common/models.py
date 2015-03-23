from django.db import models
from django.contrib.auth.models import User


#Profile de base découlant de User

class BaseProfile(models.Model):
    user = models.OneToOneField(User) #Donne les attributs de User à BaseProfile
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
        
    class Meta:
        abstract = True


#Les deux modèles héritent de BaseProfile et donc de User

class Teacher(BaseProfile):

    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):

    def __str__(self):
        return "Etudiant {0}".format(self.user.username)
        

#
# Modèle de Keran pour les cours
#

class Course(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    difficulty = models.IntegerField()
    published = models.BooleanField(default=False)
    
    author = models.ForeignKey(Teacher)
    #chapter = models.ForeignKey('teachers.Chapter', related_name="courses")
    favorites = models.ManyToManyField(User, related_name="favorite_courses", blank=True, null=True)
    # videos = models.ManyToManyField(Video)
    # images = models.ManyToManyField(Image)
    # definitions = models.ManyToManyField(Definition)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title
      
#
# Modèle de Florian pour les exercices
#

class Exercise(models.Model):
    
    owner = models.ForeignKey(Teacher)  # créateur de l'exercice   
    created_on = models.DateTimeField(auto_now_add=True) # Date de création
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30) # C'est le titre de l'exercice ( factorisation ou développement)
    equation = models.CharField(max_length=50) # C'est l'équation entrée par le professeur
    grade = models.CharField(max_length=60) # donnée une note de difficulté à l'exercice
    correction = models.CharField(max_length = 200) # Ceci est le corrigé de l'exercice ( obligatoire )
    def __str__(self):
        return self.title
        
#
# Modèle de Benoit pour les quiz
#

class Quiz(models.Model): #Infos générales sur le quiz
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=1000) #Format texte du quiz
    author = models.ForeignKey(Teacher)
    #id_chapter = models.ForeignKey('teachers.Chapter')
    
    def __str__(self):
        return self.title
        
        
        

#Modèle pour les groupes
class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher, through='GroupMembers')
    student = models.ManyToManyField(Student, through = 'GroupMembers')
    homeworkExercise = models.ManyToManyField(Exercise, through = 'AssignHomework') #uniquement les devoirs exercices
    homeworkCourse = models.ManyToManyField(Course, through = 'AssignHomework') #uniquement les devoirs quiz
    homeworkQuiz = models.ManyToManyField(Quiz, through = 'AssignHomework') #uniquement les devoirs cours
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return"Classe {0}".format(self.name)


#Table intermédiaire pour affecter un membre à un groupe

class GroupMembers(models.Model):
    teacher = models.ForeignKey(Teacher, null = True)
    student = models.ForeignKey(Student, null = True)
    group = models.ForeignKey(Group)
    added_on = models.DateTimeField(auto_now=True)
    
#Table intermédiaire pour assigner un devoir à un groupe    
    
class AssignHomework(models.Model):
    group = models.ForeignKey(Group)
    exercise = models.ForeignKey(Exercise, null = True)
    quiz = models.ForeignKey(Quiz, null = True)
    course = models.ForeignKey(Course, null = True)
    assigned_on = models.DateTimeField(auto_now=True)
    
