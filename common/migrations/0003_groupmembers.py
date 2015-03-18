# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('group', models.ForeignKey(to='common.Group')),
                ('student', models.ForeignKey(to='common.Student')),
                ('teacher', models.ForeignKey(to='common.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
