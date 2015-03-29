from django.db import models
from .. import *
from ..database.coursecatalog import CourseCatalog

class Schedule(models.Model):
    # Stuff stored by the Schedule
    lectureList = models.ManyToManyField(Lecture, null=True, blank=False, symmetrical=False)
    tutorialList = models.ManyToManyField(Tutorial, null=True, blank=False, symmetrical=False)
    labList = models.ManyToManyField(Lab, null=True, blank=False, symmetrical=False)

    # Method that returns a Python Dictionary mapping string name of subcourse_item to its event
    def view_schedule(self):
        pass

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


    # Removes an Item from the schedule
    def remove_item(self, subcourse_item):
        pass

    class Meta:
        app_label = 'app'
        managed= True

# End class Schedule