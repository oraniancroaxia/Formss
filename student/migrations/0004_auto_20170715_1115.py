# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=550),
        ),
    ]
