# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160325194918 on 2016-07-20 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_vari'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('info', models.TextField()),
            ],
        ),
    ]
