# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-05 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]
