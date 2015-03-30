# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='semester',
            field=models.CharField(default='Fall', max_length=120),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='schedule',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
