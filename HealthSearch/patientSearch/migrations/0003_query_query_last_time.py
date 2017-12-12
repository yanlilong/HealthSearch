# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientSearch', '0002_auto_20171207_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='query_last_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 10, 24, 31, 77454, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
