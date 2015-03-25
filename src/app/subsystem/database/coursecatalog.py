from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.courses.tutorial import Tutorial
from app.subsystem.courses.lab import Lab
from app.subsystem.event.event import Event
from itertools import chain


class CourseCatalog(object):

    #
    # Returns List of Courses that contain partialName in either Name or in Deptnum
    # or Department or Number
    def searchCourses(partialName):
        nospacesstring = partialName.replace(" ","")
        c1 = Course.objects.filter(name__icontains=partialName)
        c2 = Course.objects.filter(department__icontains=partialName)
        c3 = Course.objects.filter(number__icontains=partialName)
        c4 = Course.objects.filter(deptnum__icontains=nospacesstring)

        result_list = list(chain(c1, c2, c3, c4))

        return result_list

    def searchCoursesByCredits(lowerCreditLimit, upperCreditLimit):

        result_list = Course.objects.filter(credits__gte=lowerCreditLimit, credits__lte=upperCreditLimit)

        return result_list


	# Removes Course from database, removes any lecture,tut or lab under it as well
    #inputs
    # 4 letter department, case sensitive i.e SOEN
    # 3 number course number i.e 341
    #outputs true if removed, false if not
    def removeCourse(department, number):

        primarykey = department+number;
        try:
            Course.objects.get(pk=primarykey).delete()
            return True
        except Course.DoesNotExist:
            return False


	# def addCourse(name, number, department, credits, ):



    #
	# def modifyCourseCapacity(newCapacity):
	# 	pass
    #
	# def __init__(self):
	# 	pass
