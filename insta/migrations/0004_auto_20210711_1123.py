# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-11 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20210711_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='profile',
            new_name='user_profile',
        ),
    ]
