# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        RunPython('common', '0012_auto_20150317_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='student2',
            field=models.ManyToManyField(related_name='name', to='common.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher2',
            field=models.ManyToManyField(related_name='name', to='common.Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(through='common.GroupMembers', to='common.Student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(through='common.GroupMembers', to='common.Teacher'),
        ),
    ]
