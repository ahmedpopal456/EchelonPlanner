# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150417_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='previousSession',
            field=models.CharField(null=True, max_length=64),
            preserve_default=True,
        ),
    ]
