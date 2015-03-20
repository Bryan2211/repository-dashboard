# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('equation', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=60)),
                ('correction', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('added_on', models.DateField(auto_now=True)),
                ('group', models.ForeignKey(to='common.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='quiz',
            name='author',
            field=models.ForeignKey(to='common.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='student',
            field=models.ForeignKey(to='common.Student', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='teacher',
            field=models.ForeignKey(to='common.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(to='common.Student', through='common.GroupMembers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(to='common.Teacher', through='common.GroupMembers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='owner',
            field=models.ForeignKey(to='common.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(related_name='courses', to='common.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_courses', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
