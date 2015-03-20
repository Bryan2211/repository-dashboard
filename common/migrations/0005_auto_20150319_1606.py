# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150319_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('assigned_on', models.DateTimeField(auto_now=True)),
                ('Course', models.ForeignKey(to='common.Course', null=True)),
                ('exercise', models.ForeignKey(to='common.Exercise', null=True)),
                ('group', models.ForeignKey(to='common.Group')),
                ('quiz', models.ForeignKey(to='common.Quiz', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='homeworkCourse',
            field=models.ManyToManyField(through='common.AssignHomework', to='common.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='homeworkExercise',
            field=models.ManyToManyField(through='common.AssignHomework', to='common.Exercise'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='homeworkQuiz',
            field=models.ManyToManyField(through='common.AssignHomework', to='common.Quiz'),
            preserve_default=True,
        ),
    ]
