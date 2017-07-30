# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=440)),
                ('genre', models.CharField(max_length=400)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=10)),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
    ]
