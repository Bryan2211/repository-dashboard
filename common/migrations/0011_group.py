# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20150317_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
