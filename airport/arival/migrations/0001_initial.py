# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arival',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('airline', models.CharField(max_length=200)),
                ('flight_no', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('sta', models.TimeField(max_length=200)),
                ('eta', models.TimeField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'arival',
            },
        ),
    ]
