from django.db import models
from .. import *
from .schedulegenerator import ScheduleGenerator
import datetime
from ..event.event import Event
import json
#from ..database.coursecatalog import CourseCatalog


class Schedule(models.Model):
    # Stuff stored by the Schedule
    lectureList = models.ManyToManyField(Lecture, null=True, blank=False, symmetrical=False)
    tutorialList = models.ManyToManyField(Tutorial, null=True, blank=False, symmetrical=False)
    labList = models.ManyToManyField(Lab, null=True, blank=False, symmetrical=False)
    semester = models.CharField(max_length=120, default="Fall")
    year = models.IntegerField(default=1)

    # Need to create a dictionary organized by days to send to views

    def schedule_package(self):
        #TODO: Possibly won't work for online courses?
        # 0-6 corresponds to Monday-Sunday
        sectionslist = self.view_schedule()
        weekdictlist = [[],[],[],[],[],[],[]]
        weeksectionlist = [[],[],[],[],[],[],[]]

        # separate sections into separate daylists
        for section in sectionslist:
            if section.event.isMonday():
                weeksectionlist[0].append(section)
            if section.event.isTuesday():
                weeksectionlist[1].append(section)
            if section.event.isWednesday():
                weeksectionlist[2].append(section)
            if section.event.isThursday():
                weeksectionlist[3].append(section)
            if section.event.isFriday():
                weeksectionlist[4].append(section)
            if section.event.isSaturday():
                weeksectionlist[5].append(section)
            if section.event.isSunday():
                weeksectionlist[6].append(section)

        # order this based on starttime

        minstart = datetime.time(8, 45)
        maxend = datetime.time(23, 0)

        for listitem in weeksectionlist:
            listitem.sort(key=lambda x: x.event.starttime)
            blanklist = []

            #if listitem is blank, no lectures that day, must be full with full blank
            if len(listitem) == 0:
                e = Event(starttime=minstart, endtime=maxend, location="Blank")
                blankitem = Lecture(event=e)
                blanklist.append(blankitem)

            for i, item in enumerate(listitem):
                #Check if at last section in day, and if it ends at 23:00 or not
                # if not fill in blank
                # break out of for loop if last
                if i == len(listitem)-1:
                    if item.event.endtime != maxend:
                        e = Event(starttime=item.event.endtime, endtime=maxend, location="Blank")
                        blankitem = Lecture(event=e)
                        blanklist.append(blankitem)
                    break

                # Check if first item is an 8:45am class, if not fill up with blank lecture
                # Hack to set location to blank
                if i == 0:
                    if item.event.starttime != minstart:
                        e = Event(starttime=minstart, endtime=item.event.starttime, location="Blank")
                        blankitem = Lecture(event=e)
                        blanklist.append(blankitem)
                # check time difference between current item and next.
                # If not identical (rounded) then create blank between
                if item.event.getRoundedEnd() != listitem[i+1].event.getRoundedStart():
                    e = Event(starttime=item.event.endtime, endtime=listitem[i+1].event.starttime, location="Blank")
                    blankitem = Lecture(event=e)
                    blanklist.append(blankitem)

            #transfer from blanklist to listitem at end.
            for blank in blanklist:
                listitem.append(blank)
            # then resort:
            listitem.sort(key=lambda x: x.event.starttime)

        ##########testing
        # for listing in weeksectionlist:
        #     for item in listing:
        #         print(item.event.starttime, item.event.endtime, item.event.location)

        # create separate dictionaries for each day

        for i, day in enumerate(weeksectionlist):

            for block in day:
                blocktype = block.name()
                if block.event.location == "Blank":
                    blocktype = "Blank"
                if block.course is None:
                    coursename = None
                else:
                    coursename = block.course.deptnum
                weekdictlist[i].append({"RoundedStart": block.event.getRoundedStart(),
                                        "Duration": block.event.getDuration(),
                                        "Type": blocktype,
                                        "ActualStart": block.event.getActualStart(),
                                        "ActualEnd": block.event.getActualEnd(),
                                        "Location": block.event.location,
                                        "Course": coursename
                                        })


        scheduledict = {"Monday": weekdictlist[0],
                        "Tuesday": weekdictlist[1],
                        "Wednesday": weekdictlist[2],
                        "Thursday": weekdictlist[3],
                        "Friday": weekdictlist[4],
                        "Saturday": weekdictlist[5],
                        "Sunday": weekdictlist[6]
                        }

        return scheduledict
        # print(json.dumps(scheduledict))


    # Returns List of Lecture, Tutorials and Lab
    # To Use: iterate over each Type, then within each type, each section
    # for each section, access its event. Event has all that's needed for display. See Event model for description
    def view_schedule(self):

        returnlist = []

        for item in self.lectureList.all():
            returnlist.append(item)
        for item in self.tutorialList.all():
            returnlist.append(item)
        for item in self.labList.all():
            returnlist.append(item)

        return returnlist

    # Adds a Lecture/Tutorial/Lab to the schedule. Must do Type Inference to store correctly
    def add_item(self, subcourse_item):

        # Need to make sure that item does not already exist in schedule
        for item in self.lectureList.all():
            if subcourse_item.course == item.course:
                return False

        # Need to make sure it won't conflict with anything already in schedule
        if ScheduleGenerator.conflictswithlist(subcourse_item, self.labList.all()):
            return False
        if ScheduleGenerator.conflictswithlist(subcourse_item, self.tutorialList.all()):
            return False
        if ScheduleGenerator.conflictswithlist(subcourse_item, self.lectureList.all()):
            return False

        # if Lecture, must mean there isn't any lab or tutorial associated with it
        if subcourse_item.name() == "Lecture":
            self.lectureList.add(subcourse_item)
            return True

        # if Tutorial, must add tutorial and its Lecture
        if subcourse_item.name() == "Tutorial":
            self.tutorialList.add(subcourse_item)
            self.lectureList.add(subcourse_item.lecture)
            return True

        # if Lab, must add Lecture. Then must check if there are tutorials to add as well.
        if subcourse_item.name() == "Lab":
            self.lectureList.add(subcourse_item.lecture)
            self.labList.add(subcourse_item)

            if subcourse_item.tutorial is not None:
                self.tutorialList.add(subcourse_item.tutorial)
            return True

    # Removes an Item from the schedule, must provide lowest possible section Lecture > Tutorial > Lab
    def remove_item(self, subcourse_item):

        # if Lecture, must mean there isn't any lab or tutorial associated with it
        if subcourse_item.name() == "Lecture":
            self.lectureList.remove(subcourse_item)

        # if Tutorial, must add tutorial and its Lecture
        if subcourse_item.name() == "Tutorial":
            self.tutorialList.remove(subcourse_item)
            self.lectureList.remove(subcourse_item.lecture)

        # if Lab, must add Lecture. Then must check if there are tutorials to add as well.
        if subcourse_item.name() == "Lab":
            self.lectureList.remove(subcourse_item.lecture)
            self.labList.remove(subcourse_item)

            if subcourse_item.tutorial is not None:
                self.tutorialList.remove(subcourse_item.tutorial)


    class Meta:
        app_label = 'app'
        managed = True

# End class Schedule