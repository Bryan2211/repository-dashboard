# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newgroup',
            name='student',
        ),
        migrations.RemoveField(
            model_name='newgroup',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='group',
            field=models.ForeignKey(to='common.Group'),
        ),
        migrations.DeleteModel(
            name='NewGroup',
        ),
    ]
