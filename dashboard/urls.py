from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard.views import *


urlpatterns = patterns('teachers.views',
    url(r'^home/$', home, name='home'),
    url(r'^classe/(?P<group_id>\d+)/$', group, name='group_view'),
    url(r'^login/$', login, name='login'),
    url(r'^exercices/$', exercises, name='exercises'),
    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),
    url(r'^manage/exercice/$', manage, name="manage"),
    url(r'^profil/$', profil, name = 'profil'),
    #url(r'^register/$', register, name='register'),
    #url(r'^admin/', include(admin.site.urls)),
)