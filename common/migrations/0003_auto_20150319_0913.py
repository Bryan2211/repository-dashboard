# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150318_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='teacher',
            field=models.ForeignKey(to='common.Teacher', null=True),
        ),
    ]
