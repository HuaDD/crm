# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_userinfo_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Derartment', verbose_name='部门'),
        ),
    ]