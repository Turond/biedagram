# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 17:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0011_auto_20171107_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 17, 24, 50, 28047, tzinfo=utc)),
        ),
    ]