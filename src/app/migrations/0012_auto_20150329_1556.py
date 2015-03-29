# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150329_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='mainSchedule',
            field=models.ForeignKey(null=True, blank=True, to='app.Schedule', related_name='main_schedule'),
            preserve_default=True,
        ),
    ]
