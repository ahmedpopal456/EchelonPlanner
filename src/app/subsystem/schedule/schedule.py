from django.db import models
from .. import *

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
        pass

    # Removes an Item from the schedule
    def remove_item(self, subcourse_item):
        pass

    class Meta:
        app_label = 'app'
        managed= True

# End class Schedule