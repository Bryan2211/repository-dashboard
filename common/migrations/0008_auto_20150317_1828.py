# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20150317_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='student2',
            field=models.ManyToManyField(related_name='pomme', to='common.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher2',
            field=models.ManyToManyField(related_name='banane', to='common.Teacher'),
            preserve_default=True,
        ),
    ]
