# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_professor_programdirector'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='prof',
            field=models.CharField(max_length=120, default='Prof X'),
            preserve_default=True,
        ),
    ]
