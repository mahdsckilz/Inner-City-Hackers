# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='heading2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='city',
            name='para2',
            field=models.TextField(blank=True, default=''),
        ),
    ]