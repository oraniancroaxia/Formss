# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Detail',
        ),
    ]
