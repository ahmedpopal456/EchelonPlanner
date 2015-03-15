# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=120, default='A')),
                ('course', models.ForeignKey(to='app.Course')),
                ('tutorial', models.ForeignKey(to='app.Lecture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tutorial',
            unique_together=set([('section', 'course', 'tutorial')]),
        ),
    ]
