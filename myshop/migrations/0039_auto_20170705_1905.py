# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0038_auto_20170705_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=20, unique=True),
        ),
    ]
