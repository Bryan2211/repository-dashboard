# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20150317_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
