# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150317_1802'),
    ]

    operations = [
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
    ]
