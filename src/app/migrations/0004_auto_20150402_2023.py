# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150330_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='atleast_one',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='option',
            name='option',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
