# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 16:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160730_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 30, 19, 6, 15, 58883)),
        ),
    ]
