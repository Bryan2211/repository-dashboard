# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20150319_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='added_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
