# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20170728_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='closingHours',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='item',
            name='openingHours',
            field=models.CharField(default='00:00', max_length=5),
        ),
    ]
