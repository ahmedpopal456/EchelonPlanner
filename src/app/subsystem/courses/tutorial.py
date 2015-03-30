from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.event.event import Event

class Tutorial(models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False, null=True)
    lecture = models.ForeignKey(Lecture, primary_key=False, null=True)
    event = models.OneToOneField(Event, null=True)

    def __str__(self):
        return (self.section)

    def name(self):
        return "Tutorial"

    class Meta:
        unique_together = ('section', 'course', 'lecture')
        app_label = 'app'
        managed= True

# End class Tutorial