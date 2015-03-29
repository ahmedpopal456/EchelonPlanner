# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_student_academicrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('labList', models.ManyToManyField(to='app.Lab', null=True)),
                ('lectureList', models.ManyToManyField(to='app.Lecture', null=True)),
                ('tutorialList', models.ManyToManyField(to='app.Tutorial', null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
