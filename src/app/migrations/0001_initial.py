# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=120, default='Test')),
                ('department', models.CharField(max_length=120, default='SOEN')),
                ('number', models.IntegerField(default=0)),
                ('deptnum', models.CharField(max_length=120, primary_key=True, default='SOEN101', serialize=False)),
                ('type', models.CharField(max_length=120, blank=True, null=True)),
                ('credits', models.IntegerField(default=0)),
                ('yearSpan', models.CharField(max_length=120, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('section', models.CharField(max_length=120, default='A')),
                ('session', models.CharField(max_length=120, default='Fall')),
                ('isOnline', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='app.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('section', 'course')]),
        ),
    ]
