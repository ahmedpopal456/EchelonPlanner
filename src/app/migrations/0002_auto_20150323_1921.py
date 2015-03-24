# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='event',
            field=models.OneToOneField(null=True, to='app.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tutorial',
            name='event',
            field=models.OneToOneField(null=True, to='app.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='event',
            field=models.OneToOneField(null=True, to='app.Event'),
            preserve_default=True,
        ),
    ]
