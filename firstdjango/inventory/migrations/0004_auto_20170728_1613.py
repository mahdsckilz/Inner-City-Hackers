# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170728_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('1', 'College'), ('2', 'Library'), ('3', 'Industry'), ('4', 'Hotel'), ('5', 'Park'), ('6', 'Zoo'), ('7', 'Museum'), ('8', 'Restaurant'), ('9', 'Mall')], default=1, max_length=200),
        ),
    ]