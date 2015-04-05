# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150402_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cellphone',
            field=models.CharField(default='XXX-XXX-XXXX', max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='homephone',
            field=models.CharField(default='+1-XXX-XXX-XXXX', max_length=15),
            preserve_default=True,
        ),
    ]
