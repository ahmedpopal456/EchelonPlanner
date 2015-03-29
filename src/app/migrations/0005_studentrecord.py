# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150328_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('GPA', models.FloatField(default=4.0)),
                ('currentStanding', models.CharField(max_length=120, default='Good')),
                ('currentCredits', models.FloatField(default=0)),
                ('remainingCredits', models.FloatField(default=0)),
                ('academicProgram', models.ForeignKey(to='app.AcademicProgram')),
                ('coursesTaken', models.ManyToManyField(related_name='course_previously_taken', to='app.Course', blank=True, null=True)),
                ('registeredCourses', models.ManyToManyField(related_name='current_semester_course', to='app.Course', blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
