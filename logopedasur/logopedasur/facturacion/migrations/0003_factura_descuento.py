# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20160312_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='descuento',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='descuento'),
        ),
    ]
