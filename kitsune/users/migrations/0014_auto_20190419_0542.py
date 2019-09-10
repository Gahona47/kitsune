# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-19 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190304_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fxa_uid',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_fxa_migrated',
            field=models.BooleanField(default=False),
        ),
    ]