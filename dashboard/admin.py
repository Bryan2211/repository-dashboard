from django.contrib import admin
from common.models import Group, GroupMembers, Student, Teacher

admin.site.register(Group)
admin.site.register(GroupMembers)

# Register your models here.
