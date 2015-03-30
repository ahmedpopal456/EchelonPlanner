# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(default='SOEN', max_length=120)),
                ('credits', models.FloatField(default=0)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(default='Test', max_length=120)),
                ('department', models.CharField(default='SOEN', max_length=120)),
                ('number', models.IntegerField(default=0)),
                ('deptnum', models.CharField(default='SOEN101', primary_key=True, max_length=120, serialize=False)),
                ('type', models.CharField(blank=True, null=True, max_length=120)),
                ('credits', models.FloatField(default=0)),
                ('yearSpan', models.CharField(blank=True, default='14-15', null=True, max_length=120)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('days', models.CharField(default='Test', max_length=120)),
                ('starttime', models.TimeField(default=datetime.time(0, 0))),
                ('endtime', models.TimeField(default=datetime.time(0, 0))),
                ('building', models.CharField(blank=True, default='SGW H', null=True, max_length=120)),
                ('room', models.IntegerField(default=0)),
                ('location', models.CharField(default='SGW H101', max_length=120)),
                ('semester', models.CharField(max_length=120)),
                ('yearSpan', models.CharField(blank=True, null=True, max_length=120)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('section', models.CharField(default='A', max_length=120)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(null=True, to='app.Event')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('section', models.CharField(default='A', max_length=120)),
                ('session', models.CharField(default='Fall', max_length=120)),
                ('isOnline', models.BooleanField(default=False)),
                ('prof', models.CharField(default='Prof X', max_length=120)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(null=True, to='app.Event')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(default='Test', max_length=120)),
                ('option', models.IntegerField(default=1)),
                ('type', models.IntegerField(default=5)),
                ('academicprogram', models.ForeignKey(to='app.AcademicProgram')),
                ('course', models.ForeignKey(to='app.Course')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('isEngineer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgramDirector',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('department', models.CharField(default='CSE', max_length=120)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('labList', models.ManyToManyField(null=True, to='app.Lab')),
                ('lectureList', models.ManyToManyField(null=True, to='app.Lecture')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('homephone', models.IntegerField(default=0)),
                ('cellphone', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=120)),
                ('IDNumber', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('GPA', models.FloatField(default=4.0)),
                ('currentStanding', models.CharField(default='Good', max_length=120)),
                ('currentCredits', models.FloatField(default=0)),
                ('remainingCredits', models.FloatField(default=120)),
                ('academicProgram', models.ForeignKey(null=True, to='app.AcademicProgram')),
                ('coursesTaken', models.ManyToManyField(blank=True, related_name='course_previously_taken', null=True, to='app.Course')),
                ('mainSchedule', models.ForeignKey(blank=True, null=True, to='app.Schedule', related_name='main_schedule')),
                ('registeredCourses', models.ManyToManyField(blank=True, related_name='current_semester_course', null=True, to='app.Course')),
                ('scheduleCache', models.ManyToManyField(blank=True, related_name='all_generated_schedules', null=True, to='app.Schedule')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('section', models.CharField(default='A', max_length=120)),
                ('course', models.ForeignKey(null=True, to='app.Course')),
                ('event', models.OneToOneField(null=True, to='app.Event')),
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
        migrations.AddField(
            model_name='student',
            name='academicRecord',
            field=models.OneToOneField(null=True, to='app.StudentRecord'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='schedule',
            name='tutorialList',
            field=models.ManyToManyField(null=True, to='app.Tutorial'),
            preserve_default=True,
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
            field=models.ForeignKey(blank=True, null=True, to='app.Tutorial', default=None),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lab',
            unique_together=set([('section', 'course', 'lecture', 'tutorial')]),
        ),
        migrations.AddField(
            model_name='academicprogram',
            name='course',
            field=models.ManyToManyField(null=True, to='app.Course', through='app.Option'),
            preserve_default=True,
        ),
    ]
