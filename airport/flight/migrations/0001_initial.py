# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('airline', models.CharField(max_length=200)),
                ('flight_no', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('sta', models.CharField(max_length=200)),
                ('eta', models.TimeField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'flight',
            },
        ),
    ]
