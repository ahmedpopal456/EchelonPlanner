# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150328_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='remainingCredits',
            field=models.FloatField(default=120),
            preserve_default=True,
        ),
    ]
