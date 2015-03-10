# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_groupmembers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='added_on',
            field=models.DateField(auto_now=True),
        ),
    ]
