# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160918_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
