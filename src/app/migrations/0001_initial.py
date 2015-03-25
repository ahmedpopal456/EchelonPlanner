# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(default='Test', max_length=120)),
                ('department', models.CharField(default='SOEN', max_length=120)),
                ('number', models.IntegerField(default=0)),
                ('deptnum', models.CharField(default='SOEN101', max_length=120, serialize=False, primary_key=True)),
                ('type', models.CharField(blank=True, max_length=120, null=True)),
                ('credits', models.FloatField(default=0)),
                ('yearSpan', models.CharField(blank=True, max_length=120, null=True)),
                ('prerequisites', models.ManyToManyField(blank=True, null=True, to='app.Course')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('days', models.CharField(default='Test', max_length=120)),
                ('starttime', models.TimeField(default=datetime.time(0, 0))),
                ('endtime', models.TimeField(default=datetime.time(0, 0))),
                ('building', models.CharField(default='SGW H', max_length=120)),
                ('room', models.IntegerField(default=0)),
                ('location', models.CharField(default='SGW H101', max_length=120)),
                ('semester', models.CharField(max_length=120)),
                ('yearSpan', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('section', models.CharField(default='A', max_length=120)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(to='app.Event', null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('section', models.CharField(default='A', max_length=120)),
                ('session', models.CharField(default='Fall', max_length=120)),
                ('isOnline', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(to='app.Event', null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('section', models.CharField(default='A', max_length=120)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(to='app.Event', null=True)),
                ('lecture', models.ForeignKey(null=True, to='app.Lecture')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tutorial',
            unique_together=set([('section', 'course', 'lecture')]),
        ),
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('section', 'course', 'session')]),
        ),
        migrations.AddField(
            model_name='lab',
            name='lecture',
            field=models.ForeignKey(null=True, to='app.Lecture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lab',
            name='tutorial',
            field=models.ForeignKey(blank=True, to='app.Tutorial', default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lab',
            unique_together=set([('section', 'course', 'lecture', 'tutorial')]),
        ),
    ]
