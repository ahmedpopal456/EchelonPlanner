# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150327_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprogram',
            name='course',
            field=models.ManyToManyField(to='app.Course', through='app.Option', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='yearSpan',
            field=models.CharField(blank=True, null=True, max_length=120, default='14-15'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='building',
            field=models.CharField(blank=True, null=True, max_length=120, default='SGW H'),
            preserve_default=True,
        ),
    ]
