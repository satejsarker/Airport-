# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('contact', models.IntegerField()),
            ],
            options={
                'db_table': 'shop',
            },
        ),
    ]
