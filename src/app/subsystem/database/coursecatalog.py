from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.courses.tutorial import Tutorial
from app.subsystem.courses.lab import Lab
from app.subsystem.event.event import Event
from itertools import chain
import logging
import django.db

logger = logging.getLogger(__name__)


class CourseCatalog(object):
    #
    # Returns List of Courses that contain partialName in either Name or in Deptnum
    # or Department or Number
    def searchCourses(partialName):
        nospacesstring = partialName.replace(" ", "")
        c1 = set(list(Course.objects.filter(name__icontains=partialName)))
        c1.update(list(Course.objects.filter(department__icontains=partialName)))
        c1.update(list(Course.objects.filter(number__icontains=partialName)))
        c1.update(list(Course.objects.filter(deptnum__icontains=nospacesstring)))

        return list(c1)

    # either define a limit or an exact credit value to check. Limits are inclusive.
    def searchCoursesByCredits(lowerCreditLimit, upperCreditLimit=None):

        if upperCreditLimit is not None:
            result_list = Course.objects.filter(credits__gte=lowerCreditLimit, credits__lte=upperCreditLimit)
        else:
            result_list = Course.objects.filter(credits=lowerCreditLimit)

        return result_list


    # Removes Course from database, removes any lecture,tut or lab under it as well
    # inputs
    # 4 letter department, case sensitive i.e SOEN
    # 3 number course number i.e 341
    #outputs true if removed, false if not
    def removeCourse(department, number):

        primarykey = department + str(number);
        try:
            Course.objects.get(pk=primarykey).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Course")
            return False


    def modifyCredits(department, number, credits):

        try:
            C = Course.objects.get(pk=department + str(number))
            C.credits = credits
            C.save()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot modify Credits")
            return False

    def addCourse(self, name, number, department, credits=None):

        if len(Course.objects.filter(pk=department + str(number))) is not 0:
            logger.warn("Course already exists: " + department + str(number) + ". Cannot add")
            return False  # Course already exisits

        else:
            c = Course(name=name, number=number, department=department, deptnum=department + str(number))
            if credits is not None:
                c.credits = credits

            c.save()
            return True

    def addLectureToCourse(section, department, number, starttime, endtime, days, semester, location, isOnline):

        try:
            c = Course.objects.get(pk=(department + str(number)))
            e = Event(days=days, starttime=starttime, endtime=endtime, location=location,
                      semester=semester)
            e.save()
            l = Lecture(section=section, session=semester, isOnline=isOnline, event=e)
            l.save()
            c.lecture_set.add(l)
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot add to Course")
            return False
        except django.db.IntegrityError:
            logger.warn(("Lecture already in DB: {}{}, {}-{}. Cannot add to Course").format(department, number, section,
                                                                                            semester))
            return False


    def removeLecture(section, department, number, semester):  #removes any labs/tut under

        primarykey = department + str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.lecture_set.get(session=semester, section=section).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lecture.DoesNotExist:
            logger.warn(
                ("Lecture not found: {}{}, {}-{}. Cannot remove from Course").format(department, number, section,
                                                                                     semester))
            return False


    def labToCourse(self, number, section, starttime, endtime, days, semester, location, department):


        e = Event(days=days, starttime=starttime, endtime=endtime, location=location, semester=semester)
        lab = Lab(section=section, event=e)


        #Below, we try to add a lab to a course if the lab exists, otherwise we throw an exception

        try:
            c = Course.objects.get(pk=(department + str(number)))
            e.save()
            lab.save()
            c.lab_set.add(lab)

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False

        #Once the lab has been added to the course, we search for the tutorial linked with the section
        # and add try to add the lab to the tutorial
        try:
            tutoriallist = set(
                list(Tutorial.objects.filter(number=number, section=section, semester=semester, department=department)))
            tutoriallist[0].lab_set.add(lab)

        except Tutorial.DoesNotExist:
            logger.warn("Tutorial does not exist for this course")


    def removeLab(self, section, department, number, semester):

        #Try to get the course with the primary key, if it is available, delete the lab that is inside of it
        primarykey = department + str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.lab_set.get(session=semester, section=section, number=number).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lab.DoesNotExist:
            logger.warn("Lab not found, it cannot remove from Course")
            return False


    def tutorialToCourse(self, section, department, number, semester, starttime, endtime, days, location):

        try:
            c = Course.objects.get(pk=(department + str(number)))
            e = Event(days=days, starttime=starttime, endtime=endtime, location=location,
                      semester=semester)
            e.save()
            tut = Tutorial(section=section, session=semester, event=e)
            tut.save()
            c.tutorial_set.add(tut)
            return True

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot add to Course")
            return False
        except django.db.IntegrityError:
            logger.warn(
                ("Tutorial already in DB, it cannot be added to courses").format(department, number, section, semester))
            return False


    def removeTutorial(self, section, department, number, semester):

        primarykey = department + str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.tutorial_set.get(number=number, session=semester, section=section).delete()
            return True

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lecture.DoesNotExist:
            logger.warn(
                ("Lecture not found: {}{}, {}-{}. Cannot remove from Course").format(department, number, section,
                                                                                     semester))
            return False
