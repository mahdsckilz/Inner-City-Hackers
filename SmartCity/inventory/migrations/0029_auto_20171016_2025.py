# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-16 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_auto_20171016_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
