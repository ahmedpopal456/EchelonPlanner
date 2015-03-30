# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150329_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='session',
            new_name='semester',
        ),
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('section', 'course', 'semester')]),
        ),
    ]
