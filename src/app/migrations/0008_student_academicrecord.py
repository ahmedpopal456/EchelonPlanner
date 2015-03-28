# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_lecture_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='academicRecord',
            field=models.OneToOneField(to='app.StudentRecord', null=True),
            preserve_default=True,
        ),
    ]
