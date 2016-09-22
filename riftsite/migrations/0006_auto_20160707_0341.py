# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riftsite', '0005_auto_20160707_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='Human', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='subrace',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]