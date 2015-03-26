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
        nospacesstring = partialName.replace(" ","")
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
    #inputs
    # 4 letter department, case sensitive i.e SOEN
    # 3 number course number i.e 341
    #outputs true if removed, false if not
    def removeCourse(department, number):

        primarykey = department+str(number);
        try:
            Course.objects.get(pk=primarykey).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: "+department+str(number)+". Cannot remove Course")
            return False


    def modifyCredits(department, number, credits):

        try:
            C = Course.objects.get(pk=department+str(number))
            C.credits = credits
            C.save()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: "+department+str(number)+". Cannot modify Credits")
            return False

    def addCourse(name, number, department, credits=None):

        if len(Course.objects.filter(pk=department+str(number))) is not 0:
            logger.warn("Course already exists: "+department+str(number)+". Cannot add")
            return False # Course already exisits

        else:
            c = Course(name=name, number=number, department=department, deptnum=department+str(number))
            if credits is not None:
                c.credits = credits

            c.save()
            return True

    def addLectureToCourse(section, department, number, starttime, endtime, days, semester, location, isOnline):

        try:
            c = Course.objects.get(pk=(department+str(number)))
            e = Event(days =days, starttime = starttime, endtime=endtime,  location = location,
                semester = semester)
            e.save()
            l = Lecture(section=section, session = semester, isOnline=isOnline, event=e)
            l.save()
            c.lecture_set.add(l)
            return True
        except Course.DoesNotExist :
            logger.warn("Course not found: "+department+str(number)+". Cannot add to Course")
            return False
        except django.db.IntegrityError:
            logger.warn(("Lecture already in DB: {}{}, {}-{}. Cannot add to Course").format(department,number, section,semester))
            return False


    def removeLecture(section, department, number, semester): #removes any labs/tut under

        primarykey = department+str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.lecture_set.get(session =semester, section= section).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: "+department+str(number)+". Cannot remove Lecture from Course")
            return False
        except Lecture.DoesNotExist:
            logger.warn(("Lecture not found: {}{}, {}-{}. Cannot remove from Course").format(department,number, section,semester))
            return False

	# def modifyCourseCapacity(newCapacity):
	# 	pass
    #
	# def __init__(self):
	# 	pass
