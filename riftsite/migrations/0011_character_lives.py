# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riftsite', '0010_auto_20160716_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='lives',
            field=models.IntegerField(default=7),
        ),
    ]