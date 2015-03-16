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
                ('deptnum', models.CharField(serialize=False, max_length=120, primary_key=True, default='SOEN101')),
                ('type', models.CharField(max_length=120, blank=True, null=True)),
                ('credits', models.IntegerField(default=0)),
                ('yearSpan', models.CharField(max_length=120, blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('section', models.CharField(max_length=120, default='A')),
                ('session', models.CharField(max_length=120, default='Fall')),
                ('isOnline', models.BooleanField(default=False)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('section', models.CharField(max_length=120, default='A')),
                ('course', models.ForeignKey(to='app.Course')),
                ('tutorial', models.ForeignKey(to='app.Lecture')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tutorial',
            unique_together=set([('section', 'course', 'tutorial')]),
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
            field=models.ForeignKey(blank=True, null=True, to='app.Tutorial'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lab',
            unique_together=set([('section', 'course', 'lecture', 'tutorial')]),
        ),
    ]
