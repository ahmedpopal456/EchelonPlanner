from django.db import models
from .. import *
from ..database.coursecatalog import CourseCatalog

class Schedule(models.Model):
    # Stuff stored by the Schedule
    lectureList = models.ManyToManyField(Lecture, null=True, blank=False, symmetrical=False)
    tutorialList = models.ManyToManyField(Tutorial, null=True, blank=False, symmetrical=False)
    labList = models.ManyToManyField(Lab, null=True, blank=False, symmetrical=False)
    semester = models.CharField(max_length=120, default="Fall")
    year = models.IntegerField(default=1)

    # Returns list of List of Lecture, Tutorials and Lab
    # To Use in front end: iterate over each Type, then within each type, each section
    # for each section, access its event. Event has all that's needed for display. See Event model for description
    def view_schedule(self):

        returnlist = []
        returnlist.append(self.lectureList.all())
        returnlist.append(self.tutorialList.all())
        returnlist.append(self.labList.all())
        return returnlist

    # Adds a Lecture/Tutorial/Lab to the schedule. Must do Type Inference to store correctly
    def add_course(self, subcourse_item):

        # if Lecture, must mean there isn't any lab or tutorial associated with it
        if CourseCatalog.typeofSection(subcourse_item) == "Lecture":
            self.lectureList.add(subcourse_item)

        # if Tutorial, must add tutorial and its Lecture
        if CourseCatalog.typeofSection(subcourse_item) == "Tutorial":
            self.tutorialList.add(subcourse_item)
            self.lectureList.add(subcourse_item.lecture)

        # if Lab, must add Lecture. Then must check if there are tutorials to add as well.
        if CourseCatalog.typeofSection(subcourse_item) == "Lab":
            self.lectureList.add(subcourse_item.lecture)
            self.labList.add(subcourse_item)

            if subcourse_item.tutorial is not None:
                self.tutorialList.add(subcourse_item.tutorial)


    # Removes an Item from the schedule, must provide lowest possible section Lecture > Tutorial > Lab
    def remove_item(self, subcourse_item):

        # if Lecture, must mean there isn't any lab or tutorial associated with it
        if CourseCatalog.typeofSection(subcourse_item) == "Lecture":
            self.lectureList.remove(subcourse_item)

        # if Tutorial, must add tutorial and its Lecture
        if CourseCatalog.typeofSection(subcourse_item) == "Tutorial":
            self.tutorialList.remove(subcourse_item)
            self.lectureList.remove(subcourse_item.lecture)

        # if Lab, must add Lecture. Then must check if there are tutorials to add as well.
        if CourseCatalog.typeofSection(subcourse_item) == "Lab":
            self.lectureList.remove(subcourse_item.lecture)
            self.labList.remove(subcourse_item)

            if subcourse_item.tutorial is not None:
                self.tutorialList.remove(subcourse_item.tutorial)


    class Meta:
        app_label = 'app'
        managed= True

# End class Schedule