# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('student', models.ManyToManyField(to='common.Student')),
                ('teacher', models.ManyToManyField(to='common.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
