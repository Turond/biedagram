# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 17:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_auto_20171105_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 5, 17, 44, 51, 669847, tzinfo=utc)),
        ),
    ]