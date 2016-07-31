# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 15:39
from __future__ import unicode_literals

import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160730_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='image',
            field=models.ImageField(default='settings.MEDIA_ROOT/media/rainbow.jpg', storage=django.core.files.storage.FileSystemStorage(location='/Users/brica1000/theProject/theDatabase/media'), upload_to='media'),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 30, 18, 39, 13, 50097)),
        ),
    ]