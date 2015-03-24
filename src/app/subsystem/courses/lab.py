
from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.courses.tutorial import Tutorial
from app.subsystem.event.event import Event


class Lab (models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False, null=True)
    tutorial = models.ForeignKey(Tutorial, primary_key=False, null=True, blank=True)
    lecture = models.ForeignKey(Lecture, primary_key=False, null=True)
    event = models.OneToOneField(Event, null=True)


    class Meta:
        unique_together = ('section', 'course', 'lecture', 'tutorial')
        app_label = 'app'
        managed= True