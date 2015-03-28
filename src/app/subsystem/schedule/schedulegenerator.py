from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.courses.tutorial import Tutorial
from app.subsystem.courses.lab import Lab
from app.subsystem.event.event import Event
from itertools import chain
import logging
import django.db

logger = logging.getLogger(__name__)


class ScheduleGenerator(object):

    def generateSchedules(self, preferences):
        pass

    def doDaysConflict(days1, days2):

        #Online courses no conflict
        if "-------" in days1:
            return False
        if "-------" in days2:
            return False

        #ignore weekends

        for i in range(len(days1)):
            if(days1[i] == days2[i]) and not days1[i]=='-':
                return True

        return False

    """
    Takes two sections, and determines if time conflicts. Sections can be of any type, lecture/tut/lab
    """

    def doTimesConflict(section1, section2):

        if section1.event.starttime < section2.event.endtime and section1.event.endtime > section2.event.starttime:
            return True
        else:
            return False

    #TODO: Also incomplete, not sure if we even need
    def comparetoLabTutLect(section1,section2):

        daysfor1 = section1.event.days

        if "Lab" in type(section2):
            #check for conflict in lab
            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                if ScheduleGenerator.doTimesConflict(section1, section2):
                    return True
            # switch to tutorial if no conflict in lab
            else:
                if section2.tutorial is not None:
                    section2 = section2.tutorial
                    if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                        if ScheduleGenerator.doTimesConflict(section1, section2):
                            return True
                        # go to lecture
                        else:
                            section2 = section2.course
                            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                                if ScheduleGenerator.doTimesConflict(section1, section2):
                                    return True
                # no tutorial, go straight to lecture
                else:
                    section2 = section2.course
                    if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                        if ScheduleGenerator.doTimesConflict(section1, section2):
                            return True






	# take 1 lab and compare with another lab, or tutorial if no lab
    # or lecture if no lab/tut
    #TODO: This isn't complete, not sure if we still need this
    def conflicts(section1, section2):

        if "Lecture" in type(section2):
            lecture2days = section2.event.days
            ConflictStatus = ScheduleGenerator.doDaysConflict(section1, section2)

            return ConflictStatus

        #identify what section1 and section 2 are

        if "Lab" in type(section1):

            lab1days = section1.event.days

            if "Lab" in type(section2):
                lab2days = section2.event.days

    """
    coursename is pk deptnum i.e SOEN341
    section is object of type tutorial or lab or lecture, whatever is lowest
    :returns: a list of the lowest type (lab < tutorial < lecture) that the course has that does not conflict
              with the section
    """
    def findUnconflictingSections(self, section, coursename):

        course = Course.objects.get(pk=coursename)

        typeofsection = str(type(section))
        semester = section.event.semester
        lecturesection = None
        tutorialsection = None
        labsection = None

        sectionsthatdontconflict = []
        nolecturesconf = course.lecture_set.all().filter(event__semester = semester)  # set initially to all lectures in course
        notutconf = []
        nolabconf = []
        lecturestoremove = []
        tutorialtoremove = []
        labstoremove = []

        hasLabs = True
        hasTut = True

        hasLabs = len(course.lab_set.all()) is not 0
        hasTut = len(course.tutorial_set.all()) is not 0

        if "Lecture" in typeofsection:
            # section has no lab or tutorial
            lecturesection = section
        else:
            lecturesection = section.lecture
            #lab is section, then check if a tutorial exists
            if "Lab" in typeofsection:
                labsection = section;
                if labsection.tutorial is not None:
                    tutorialsection = labsection.tutorial
            #else must be tutorial
            else:
                tutorialsection = section


        for lecture in nolecturesconf:
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days , lecture.event.days):
                if ScheduleGenerator.doTimesConflict(lecturesection, lecture):
                    lecturestoremove.append(lecture)
            if tutorialsection is not None:
                if ScheduleGenerator.doDaysConflict(tutorialsection.event.days, lecture.event.days):
                    if ScheduleGenerator.doTimesConflict(tutorialsection, lecture):
                        lecturestoremove.append(lecture)
            if labsection is not None:
                if ScheduleGenerator.doDaysConflict(labsection.event.days, lecture.event.days):
                    if ScheduleGenerator.doTimesConflict(labsection, lecture):
                        lecturestoremove.append(lecture)

        nolecturesconf = [lecture for lecture in nolecturesconf if lecture not in lecturestoremove]

        if len(nolecturesconf) is 0:
            return []

        if not hasTut and not hasLabs:
            return nolecturesconf


        for lecture in nolecturesconf:
            for tutorial in lecture.tutorial_set.all():
                notutconf.append(tutorial)


        for tutorial in notutconf:
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days , tutorial.event.days):
                if ScheduleGenerator.doTimesConflict(lecturesection, tutorial):
                    tutorialtoremove.append(tutorial)
            if tutorialsection is not None:
                if ScheduleGenerator.doDaysConflict(tutorialsection.event.days, tutorial.event.days):
                    if ScheduleGenerator.doTimesConflict(tutorialsection, tutorial):
                        tutorialtoremove.append(tutorial)
            if labsection is not None:
                if ScheduleGenerator.doDaysConflict(labsection.event.days, tutorial.event.days):
                    if ScheduleGenerator.doTimesConflict(labsection, tutorial):
                        tutorialtoremove.append(tutorial)

        notutconf = [tutorial for tutorial in notutconf if tutorial not in tutorialtoremove]

        if len(notutconf) is 0 and hasTut:
            return []

        if not hasLabs:
            return notutconf

        if hasTut:
            for tutorial in notutconf:
                for lab in tutorial.lab_set.all():
                    nolabconf.append(lab)
        else:
            for lecture in nolecturesconf:
                for lab in lecture.lab_set.all():
                    nolabconf.append(lab)


        for lab in nolabconf:
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days , lab.event.days):
                if ScheduleGenerator.doTimesConflict(lecturesection, lab):
                    labstoremove.append(lab)
            if tutorialsection is not None:
                if ScheduleGenerator.doDaysConflict(tutorialsection.event.days, lab.event.days):
                    if ScheduleGenerator.doTimesConflict(tutorialsection, lab):
                        labstoremove.append(lab)
            if labsection is not None:
                if ScheduleGenerator.doDaysConflict(labsection.event.days, lab.event.days):
                    if ScheduleGenerator.doTimesConflict(labsection, lab):
                        labstoremove.append(lab)

        nolabconf = [lab for lab in nolabconf if lab not in labstoremove]

        if len(nolabconf) is 0 and hasLabs:
            return []


        return nolabconf





    def __init__(self):
        self.studentPreferences = None


