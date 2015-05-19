# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_assignhomework_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='invite_id',
            field=models.CharField(null=True, max_length=12),
            preserve_default=True,
        ),
    ]
