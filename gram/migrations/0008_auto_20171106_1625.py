# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 16:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0007_auto_20171106_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 16, 25, 25, 424807, tzinfo=utc)),
        ),
    ]
