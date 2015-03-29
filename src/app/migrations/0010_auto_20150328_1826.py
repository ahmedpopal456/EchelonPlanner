# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='mainSchedule',
            field=models.ForeignKey(null=True, related_name='main_schedule', to='app.Schedule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studentrecord',
            name='scheduleCache',
            field=models.ManyToManyField(null=True, related_name='all_generated_schedules', blank=True, to='app.Schedule'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='academicProgram',
            field=models.ForeignKey(to='app.AcademicProgram', null=True),
            preserve_default=True,
        ),
    ]
