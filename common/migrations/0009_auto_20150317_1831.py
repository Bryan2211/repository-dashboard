# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20150317_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('student', models.ManyToManyField(to='common.Student', through='common.GroupMembers')),
                ('teacher', models.ManyToManyField(to='common.Teacher', through='common.GroupMembers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='group',
            name='student2',
        ),
        migrations.RemoveField(
            model_name='group',
            name='teacher2',
        ),
        migrations.AlterField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(to='common.Student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(to='common.Teacher'),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='group',
            field=models.ForeignKey(to='common.NewGroup'),
        ),
    ]
