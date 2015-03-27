from django.db import models
from app.subsystem.courses.course import Course

class AcademicProgram(models.Model):


    def __str__(self):
        return self.name

    name = models.CharField(max_length=120, null=False, blank=False, default="SOEN", primary_key=False)
    credits = models.FloatField(default=0, primary_key=False)
    course = models.ManyToManyField(Course, null=True, through='Option')

    class Meta:
        app_label = 'app'
        managed= True



