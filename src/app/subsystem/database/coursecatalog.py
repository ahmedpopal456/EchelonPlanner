from app.subsystem.courses.course import Course
from app.subsystem.courses.lecture import Lecture
from app.subsystem.courses.tutorial import Tutorial
from app.subsystem.courses.lab import Lab
from app.subsystem.event.event import Event
from itertools import chain


class CourseCatalog(object):


    # Returns List of Courses that contain partialName in either Name or in Deptnum
    #or Department or Number
     def searchCourses(partialName):
        nospacesstring = partialName.replace(" ","")
        c1 = Course.objects.filter(name__icontains=partialName)
        c2 = Course.objects.filter(department__icontains=partialName)
        c3 = Course.objects.filter(number__icontains=partialName)
        c4 = Course.objects.filter(deptnum__icontains=nospacesstring)

        result_list = list(chain(c1, c2, c3, c4))

        return result_list

	# def addCourse(, name, number):
	# 	pass
    #
	# def removeCourse(, name, number):
	# 	pass
    #
	# def modifyCourseCapacity(newCapacity):
	# 	pass
    #
	# def __init__(self):
	# 	pass


