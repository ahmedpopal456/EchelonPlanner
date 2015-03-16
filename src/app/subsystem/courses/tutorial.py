from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture

class Tutorial(models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False)
    tutorial = models.ForeignKey(Lecture, primary_key=False)

    class Meta:
        unique_together = ('section', 'course', 'tutorial')
        app_label = 'app'
        managed= True