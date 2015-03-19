from django.contrib import admin
from common.models import Group, GroupMembers, Student, Teacher, Exercise, Course, Quiz, AssignHomework

admin.site.register(Group)
admin.site.register(GroupMembers)
admin.site.register(Exercise)
admin.site.register(Quiz)
admin.site.register(Course)
admin.site.register(AssignHomework)

# Register your models here.
