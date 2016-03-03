# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terapeutas', '0003_auto_20160226_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='terapeuta',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
