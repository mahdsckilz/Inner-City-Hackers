# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20170728_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='amount',
        ),
    ]
