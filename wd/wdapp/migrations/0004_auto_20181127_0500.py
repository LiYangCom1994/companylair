# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wdapp', '0003_auto_20181127_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='company_id',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='c_id', to='wdapp.Company'),
        ),
    ]
