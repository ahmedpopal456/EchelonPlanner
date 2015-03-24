
from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.event.event import Event

class Lecture(models.Model):

    def __str__(self):
        return (self.section)

    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False, null=True)
    session = models.CharField(max_length=120, default="Fall", primary_key=False)
    isOnline = models.BooleanField(default=False, primary_key=False)
    event = models.OneToOneField(Event, null=True)


    class Meta:
        unique_together = ('section', 'course', 'session')
        app_label = 'app'
        managed= True
