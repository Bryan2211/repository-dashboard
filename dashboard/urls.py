from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard.views import *


urlpatterns = patterns('teachers.views',
    url(r'^home/$', home, name='home'),
    url(r'^classe/(?P<group_id>\d+)/$', group, name='group_view'),
    url(r'^exercices/$', exercises, name='exercises'),
    url(r'^nouveau_groupe/$', newgroup, name='newgroup'),
    url(r'^profil/$', profil, name = 'profil'),
    #Pour retirer d'un groupe
    url(r'^enlever_groupe/(?P<group_id>\d+)/(?P<member_id>\d+)/$', deleteFromGroup, name = "deleteFromGroup"),
    #Pour supprimer une activité
    url(r'^enlever_activité/(?P<activity_id>\d+)/$', deleteActivity, name = "deleteActivity"),
    #Pour retirer un devoir
    url(r'^enlever_devoir/(?P<group_id>\d+)/(?P<homework_id>\d+)/$', deleteHomework, name = "deleteHomework"),
)