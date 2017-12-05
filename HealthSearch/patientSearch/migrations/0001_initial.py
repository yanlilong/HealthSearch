# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.FileField(max_length=15, upload_to=b'')),
                ('url', models.URLField()),
                ('freq', models.IntegerField()),
                ('published_time', models.DateTimeField()),
                ('descrip', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('sympo', models.TextField()),
                ('disease', models.TextField()),
                ('freq', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Query_ResultURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_id', models.ForeignKey(to='patientSearch.Query')),
            ],
        ),
        migrations.CreateModel(
            name='ResultURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shorten_url', models.URLField()),
                ('result_url', models.URLField()),
                ('published_time', models.DateTimeField()),
                ('title', models.TextField()),
                ('freq', models.IntegerField()),
                ('clicks', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='query_resulturl',
            name='resulturl_id',
            field=models.ForeignKey(to='patientSearch.ResultURL'),
        ),
    ]
