from django.db import models
from django_enumfield import enum
from app.subsystem.courses.course import Course
from app.subsystem.courses.academicprogram import AcademicProgram

class OptionChoices(enum.Enum):
    NOOPTION = 0
    GAMES = 1
    WEB = 2
    AVIONICS = 3
    GENERAL = 4
# End OptionChoices

class TypeChoices(enum.Enum):
    GENERAL_ELECTIVES = 5
    REQUIRED = 6
    SCIENCE = 7
    TECHNICAL = 8
# End TypeChoices

class Option(models.Model):

    # name = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    #credits = models.IntegerField(null=False, blank=False, default=0, primary_key=False)   (implementation for this not needed in this anymore)
    option = enum.EnumField(OptionChoices, default=OptionChoices.NOOPTION)
    type = enum.EnumField(TypeChoices, default=TypeChoices.GENERAL_ELECTIVES)
    course = models.ForeignKey(Course)
    academicprogram = models.ForeignKey(AcademicProgram)
    atleast_one = models.BooleanField(default=False)

    def __str__(self):
        return self.option

    class Meta:
        app_label = 'app'
        managed= True

# End class Option