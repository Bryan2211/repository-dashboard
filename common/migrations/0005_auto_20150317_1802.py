# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150310_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(to='common.Student', through='common.GroupMembers'),
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(to='common.Teacher', through='common.GroupMembers'),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='student',
            field=models.ForeignKey(null=True, to='common.Student'),
        ),
    ]
