# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riftsite', '0008_character_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='exp',
            field=models.IntegerField(default=0),
        ),
    ]
