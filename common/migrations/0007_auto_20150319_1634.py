# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20150319_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignhomework',
            old_name='Course',
            new_name='course',
        ),
    ]
