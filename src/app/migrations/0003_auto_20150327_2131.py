# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='IDNumber',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
