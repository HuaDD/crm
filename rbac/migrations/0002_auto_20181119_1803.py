# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='alias_url',
            field=models.CharField(max_length=64, unique=True, verbose_name='URL别名'),
        ),
    ]