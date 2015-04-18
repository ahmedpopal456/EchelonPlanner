# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150405_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='mainSchedule',
            field=models.OneToOneField(to='app.Schedule', null=True, blank=True, related_name='main_schedule'),
            preserve_default=True,
        ),
    ]
