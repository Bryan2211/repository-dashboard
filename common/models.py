from django.db import models
from django.contrib.auth.models import User

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
        
    class Meta:
        abstract = True

class Teacher(BaseProfile):

    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):

    def __str__(self):
        return "Etudiant {0}".format(self.user.username)

class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher, through='GroupMembers')
    student = models.ManyToManyField(Student, through = 'GroupMembers')
    #homework = models.ManyToManyField("Exercise")
    created_on = models.DateTimeField(auto_now=True)
    
class GroupMembers(models.Model):
    teacher = models.ForeignKey(Teacher)
    student = models.ForeignKey(Student, null = True)
    group = models.ForeignKey(Group)
    added_on = models.DateField(auto_now=True)
    