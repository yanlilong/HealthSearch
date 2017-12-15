# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patientSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultURL_DataResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_resource', models.ForeignKey(to='patientSearch.DataResource',on_delete=models.DO_NOTHING)),
            ],
        ),
        migrations.RenameField(
            model_name='query_resulturl',
            old_name='query_id',
            new_name='query',
        ),
        migrations.RenameField(
            model_name='query_resulturl',
            old_name='resulturl_id',
            new_name='result_url',
        ),
        migrations.AddField(
            model_name='resulturl',
            name='last_update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 7, 9, 12, 2, 265291, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resulturl_dataresource',
            name='result_url',
            field=models.ForeignKey(to='patientSearch.ResultURL',on_delete=models.DO_NOTHING),
        ),
    ]
