# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_auto_20171017_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='image',
            field=models.ImageField(null=True, storage='college/', upload_to='college/'),
        ),
    ]
