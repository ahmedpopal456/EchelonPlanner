
from django.db import models
from app.subsystem.courses.course import Course

class Lecture(models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False)
    session = models.CharField(max_length=120, default="Fall", primary_key=False)
    isOnline = models.BooleanField(default=False, primary_key=False)


    class Meta:
        unique_together = ('section', 'course')
        app_label = 'app'
        managed= True
