# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0005_auto_20171105_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 5, 18, 7, 8, 25157, tzinfo=utc)),
        ),
    ]