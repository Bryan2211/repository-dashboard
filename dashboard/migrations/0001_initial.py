# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('success', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True, parent_link=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('e_mail', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True, parent_link=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('e_mail', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(to='dashboard.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(to='dashboard.Teacher'),
            preserve_default=True,
        ),
    ]
