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
                ('name', models.CharField(max_length=120, default='Test')),
                ('department', models.CharField(max_length=120, default='SOEN')),
                ('number', models.IntegerField(default=0)),
                ('deptnum', models.CharField(primary_key=True, serialize=False, max_length=120, default='SOEN101')),
                ('type', models.CharField(null=True, max_length=120, blank=True)),
                ('credits', models.FloatField(default=0)),
                ('yearSpan', models.CharField(null=True, max_length=120, blank=True)),
                ('prerequisites', models.ManyToManyField(related_name='prerequisites_rel_+', to='app.Course', null=True, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=120, default='Test')),
                ('starttime', models.TimeField(default=datetime.time(0, 0))),
                ('endtime', models.TimeField(default=datetime.time(0, 0))),
                ('building', models.CharField(max_length=120, default='SGW H')),
                ('room', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=120, default='SGW H101')),
                ('semester', models.CharField(max_length=120)),
                ('yearSpan', models.CharField(null=True, max_length=120, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=120, default='A')),
                ('course', models.ForeignKey(to='app.Course')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=120, default='A')),
                ('session', models.CharField(max_length=120, default='Fall')),
                ('isOnline', models.BooleanField(default=False)),
                ('event', models.TimeField(default='0:00')),
                ('course', models.ForeignKey(to='app.Course')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=120, default='A')),
                ('course', models.ForeignKey(to='app.Course')),
                ('lecture', models.ForeignKey(to='app.Lecture')),
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
            unique_together=set([('section', 'course')]),
        ),
        migrations.AddField(
            model_name='lab',
            name='lecture',
            field=models.ForeignKey(to='app.Lecture'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lab',
            name='tutorial',
            field=models.ForeignKey(null=True, to='app.Tutorial', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lab',
            unique_together=set([('section', 'course', 'lecture', 'tutorial')]),
        ),
    ]
