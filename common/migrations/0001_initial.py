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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('added_on', models.DateField(auto_now=True)),
                ('group', models.ForeignKey(to='common.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='groupmembers',
            name='student',
            field=models.ForeignKey(null=True, to='common.Student'),
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
            field=models.ManyToManyField(through='common.GroupMembers', to='common.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(through='common.GroupMembers', to='common.Teacher'),
            preserve_default=True,
        ),
    ]
