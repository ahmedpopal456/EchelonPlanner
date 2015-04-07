from ..courses.course import Course
from ..courses.lecture import Lecture
from ..courses.tutorial import Tutorial
from ..courses.lab import Lab
from ..event.event import Event
from itertools import chain
import logging
import django.db

logger = logging.getLogger(__name__)


class ScheduleGenerator(object):
    def generateSchedules(self, preferences):
        pass

    @staticmethod
    def doDaysConflict(days1, days2):

        # Online courses no conflict
        if "-------" in days1:
            return False
        if "-------" in days2:
            return False

        #ignore weekends

        for i in range(len(days1)):
            if (days1[i] == days2[i]) and not days1[i] == '-':
                return True

        return False

    # end doDaysConflict

    """
    Takes two sections, and determines if time conflicts. Sections can be of any type, lecture/tut/labt
    """

    @staticmethod
    def doTimesConflict(section1, section2):

        if section1.event.starttime < section2.event.endtime and section1.event.endtime > section2.event.starttime:
            return True
        else:
            return False

    # end doTimesConflict

    @staticmethod
    def comparetoLabTutLect(section1, section2):

        daysfor1 = section1.event.days

        if section2.name() == "Lab":
            #check for conflict in lab
            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                if ScheduleGenerator.doTimesConflict(section1, section2):
                    return True
            # switch to tutorial if no conflict in lab

            if section2.tutorial is not None:
                section2 = section2.tutorial
                if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                    if ScheduleGenerator.doTimesConflict(section1, section2):
                        return True
                    # go to lecture
                    else:
                        section2 = section2.lecture
                        if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                            if ScheduleGenerator.doTimesConflict(section1, section2):
                                return True
            # no tutorial, go straight to lecture
            else:
                section2 = section2.lecture
                if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                    if ScheduleGenerator.doTimesConflict(section1, section2):
                        return True
        elif section2.name() == "Tutorial":
            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                if ScheduleGenerator.doTimesConflict(section1, section2):
                    return True
            # switch to lecture if no conflict in tutorial
            section2 = section2.lecture
            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                    if ScheduleGenerator.doTimesConflict(section1, section2):
                        return True
        elif section2.name() == "Lecture":
            if ScheduleGenerator.doDaysConflict(daysfor1, section2.event.days):
                    if ScheduleGenerator.doTimesConflict(section1, section2):
                        return True

        # If nothing conflicts, it will get here
        return False


    # take 1 section and compare with another lab, or tutorial if no lab
    # or lecture if no lab/tut
    # end compareLabTutLect

    #TODO: This isn't complete, not sure if we still need this
    @staticmethod
    def conflicts(section1, section2):

        if section1.name() == "Lecture":  # Compare Lecture to rest, nothing should be under lecture.
            if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                return True
        elif section1.name() == "Tutorial": # Compare to Tutorial and Lecture
            if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                return True
            else:
                section1 = section1.lecture
                if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                    return True
        elif section1.name() == "Lab": # Compare to Lab, Tutorial if exists, and Lecture
            if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                return True
            # check tutorial if it exists
            if section1.tutorial is not None:
                section1 = section1.tutorial
                if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                    return True
            # Move to Lecture either way
            section1 = section1.lecture
            if(ScheduleGenerator.comparetoLabTutLect(section1, section2)):
                return True

        # if we get here, no conflicts
        return False

    # end conflicts

    @staticmethod
    def conflictswithlist(section, sectionlist):

        for item in sectionlist:
            if ScheduleGenerator.conflicts(section, item):
                return True

        # finishes loop, and no return. Good to add:
        return False

    """
    coursename is pk deptnum i.e SOEN341
    section is object of type tutorial or lab or lecture, whatever is lowest
    :returns: a list of the lowest type (lab < tutorial < lecture) that the course has that does not conflict
              with the section
    """

    @staticmethod
    def findUnconflictingSections(section, coursename):

        course = Course.objects.get(pk=coursename)

        typeofsection = str(type(section))
        semester = section.event.semester
        lecturesection = None
        tutorialsection = None
        labsection = None

        sectionsthatdontconflict = []
        nolecturesconf = course.lecture_set.all().filter(
            event__semester=semester)  # set initially to all lectures in course
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
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days, lecture.event.days):
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
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days, tutorial.event.days):
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
            if ScheduleGenerator.doDaysConflict(lecturesection.event.days, lab.event.days):
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
        # end findUnconflictingSections

        # noinspection PyUnreachableCode
        """
            Method that takes a list of courses and a semester, and returns a
            list of sections that would not conflict, if such a list exists.
            If no such list of unconflicting courses exists, an empty list
            will be returned.

            As it is implemented now, the limit on the number of courses is 6.
        """

    @staticmethod
    def findUnconflictingSectionsForOneSemester(coursesList, semester):
        courses = []
        i = 0
        while i < len(coursesList):
            if coursesList[i].hasLabs():
                courses.append(coursesList[i].lab_set.all().filter(event__semester=semester))
                i += 1
            elif coursesList[i].hasTutorials():
                courses.append(coursesList[i].tutorial_set.all().filter(event__semester=semester))
                i += 1
            else:
                courses.append(coursesList[i].lecture_set.all().filter(event__semester=semester))
                i += 1

        courseIterator = 0
        for section0 in courses[courseIterator]:
            courseIterator = 1
            sections1 = ScheduleGenerator.findUnconflictingSections(section0, coursesList[courseIterator].deptnum)
            # sections0 has the unconflicting sections between the 2 first courses
            # verify that there is another course to check, else return sections1
            if len(courses) is 2 and len(sections1) is not 0:
                sections1 = [sections1[0], section0]
                return sections1
            for section1 in sections1:
                courseIterator = 2
                sections2_0 = ScheduleGenerator.findUnconflictingSections(section0, coursesList[courseIterator].deptnum)
                sections2_1 = ScheduleGenerator.findUnconflictingSections(section1, coursesList[courseIterator].deptnum)
                # sections2 = intersection(sections2_0, sections2_1)
                sections2 = [val for val in sections2_0 if val in sections2_1]
                # sections2 = [sections2[0],section1]
                # sections2 has the unconflicting sections between the 3 first courses
                # verify that there is another course to check, else return sections2
                if len(courses) is 3 and len(sections2) is not 0:
                    sections2 = [sections2[0], section1, section0]
                    return sections2
                for section2 in sections2:
                    courseIterator = 3
                    sections3_0 = ScheduleGenerator.findUnconflictingSections(section0,
                                                                              coursesList[courseIterator].deptnum)
                    sections3_1 = ScheduleGenerator.findUnconflictingSections(section1,
                                                                              coursesList[courseIterator].deptnum)
                    sections3_2 = ScheduleGenerator.findUnconflictingSections(section2,
                                                                              coursesList[courseIterator].deptnum)
                    # sections3 = intersection(sections3_0, sections3_1, sections3_2)
                    sections3 = [val for val in sections3_0 if val in sections3_1]
                    sections3 = [val for val in sections3 if val in sections3_2]
                    # sections3 has the unconflicting sections between the 4 first courses
                    # verify that there is another course to check, else return sections3
                    if len(courses) is 4 and len(sections3) is not 0:
                        sections3 = [sections3[0], section2, section1, section0]
                        return sections3
                    for section3 in sections3:
                        courseIterator = 4
                        sections4_0 = ScheduleGenerator.findUnconflictingSections(section0,
                                                                                  coursesList[courseIterator].deptnum)
                        sections4_1 = ScheduleGenerator.findUnconflictingSections(section1,
                                                                                  coursesList[courseIterator].deptnum)
                        sections4_2 = ScheduleGenerator.findUnconflictingSections(section2,
                                                                                  coursesList[courseIterator].deptnum)
                        sections4_3 = ScheduleGenerator.findUnconflictingSections(section3,
                                                                                  coursesList[courseIterator].deptnum)
                        # sections4 = intersection(sections4_0, sections4_1, sections4_2, sections4_3)
                        sections4 = [val for val in sections4_0 if val in sections4_1]
                        sections4 = [val for val in sections4 if val in sections4_2]
                        sections4 = [val for val in sections4 if val in sections4_3]
                        # sections4 has the unconflicting sections between the 5 first courses
                        # verify that there is another course to check, else return sections4
                        if len(courses) is 5 and len(sections4) is not 0:
                            sections4 = [sections4[0], section3, section2, section1, section0]
                            return sections4
                        for section4 in sections4:
                            courseIterator = 5
                            sections5_0 = ScheduleGenerator.findUnconflictingSections(section0, coursesList[
                                courseIterator].deptnum)
                            sections5_1 = ScheduleGenerator.findUnconflictingSections(section1, coursesList[
                                courseIterator].deptnum)
                            sections5_2 = ScheduleGenerator.findUnconflictingSections(section2, coursesList[
                                courseIterator].deptnum)
                            sections5_3 = ScheduleGenerator.findUnconflictingSections(section3, coursesList[
                                courseIterator].deptnum)
                            sections5_4 = ScheduleGenerator.findUnconflictingSections(section4, coursesList[
                                courseIterator].deptnum)
                            # sections5 = intersection(sections5_0, sections5_1, sections5_2, sections5_3, sections5_4)
                            sections5 = [val for val in sections5_0 if val in sections5_1]
                            sections5 = [val for val in sections5 if val in sections5_2]
                            sections5 = [val for val in sections5 if val in sections5_3]
                            sections5 = [val for val in sections5 if val in sections5_4]
                            # sections5 has the unconflicting sections between all 6 courses
                            # verify that there is another course to check, else return sections5
                            if len(courses) is 6 and len(sections5) is not 0:
                                sections5 = [sections5[0], section4, section3, section2, section1, section0]
                                return sections5

        # if we get here by magic, there are no unconflicting schedules
        return []

    # end findUnconflictingSectionsForOneSemester


    def __init__(self):
        self.studentPreferences = None


