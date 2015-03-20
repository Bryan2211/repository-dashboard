from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard.views import *


urlpatterns = patterns('teachers.views',
    url(r'^home/$', home, name='home'),
    url(r'^classe/(?P<group_id>\d+)/$', group, name='group_view'),
    url(r'^login/$', login, name='login'),
    url(r'^exercices/$', exercises, name='exercises'),
    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),
    url(r'^profil/$', profil, name = 'profil'),
    url(r'^enlever_groupe/(?P<group_id>\d+)/(?P<member_id>\d+)/$', deleteFromGroup, name = "deleteFromGroup"),
    url(r'^enlever_activité/(?P<activity_id>\d+)/$', deleteActivity, name = "deleteActivity"),
    url(r'^enlever_devoir/(?P<group_id>\d+)/(?P<homework_id>\d+)/$', deleteHomework, name = "deleteHomework"),
    url(r'^obtenir_date/(?P<group_id>\d+)/(?P<member_id>\d+)/$', added_onDate, name = "added_onDate"),
    #url(r'^register/$', register, name='register'),
    #url(r'^admin/', include(admin.site.urls)),
)