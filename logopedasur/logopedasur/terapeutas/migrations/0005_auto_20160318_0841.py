# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapeutas', '0004_terapeuta_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terapeuta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
