# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_auto_20171013_0311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchgroup',
            options={'verbose_name_plural': 'Search Groups'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='searchGroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.SearchGroup'),
        ),
    ]
