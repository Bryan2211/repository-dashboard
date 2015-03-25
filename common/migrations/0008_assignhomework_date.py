# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20150319_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignhomework',
            name='date',
            field=models.CharField(max_length=20, default='Demain'),
            preserve_default=True,
        ),
    ]
