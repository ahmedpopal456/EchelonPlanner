# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150323_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='course',
            field=models.ForeignKey(to='app.Course', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lab',
            name='lecture',
            field=models.ForeignKey(to='app.Lecture', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.OneToOneField(to='app.Course', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='course',
            field=models.ForeignKey(to='app.Course', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='lecture',
            field=models.ForeignKey(to='app.Lecture', null=True),
            preserve_default=True,
        ),
    ]
