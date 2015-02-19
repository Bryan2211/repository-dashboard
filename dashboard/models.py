from django.db import models
from django.contrib.auth.models import User

class Student(User):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    #done_skills = models.ManyToManyField('Skill')
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
        
class Teacher(User):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)
    #homework = models.ManyToManyField("Exercise")
    success = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
