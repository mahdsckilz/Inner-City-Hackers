# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20170728_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name_plural': 'Libraries'},
        ),
    ]