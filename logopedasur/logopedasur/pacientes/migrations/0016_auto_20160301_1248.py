# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0015_auto_20160301_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=b'/uploads/'),
        ),
    ]
