from ..courses.course import Course
from ..courses.lecture import Lecture
from ..courses.tutorial import Tutorial
from ..courses.lab import Lab
from ..event.event import Event
import json
from ..usermanagement.student.student import Student
from ..usermanagement.student.student import StudentRecord
from itertools import chain
import logging
import django.db

logger = logging.getLogger(__name__)


class CourseCatalog(object):
    #
    # Returns List of Courses that contain partialName in either Name or in Deptnum
    # or Department or Number
    @staticmethod
    def searchCoursesThroughPartialName(partialName):
        nospacesstring = partialName.replace(" ", "")
        c1 = set(list(Course.objects.filter(name__icontains=partialName)))
        c1.update(list(Course.objects.filter(department__icontains=partialName)))
        c1.update(list(Course.objects.filter(number__icontains=partialName)))
        c1.update(list(Course.objects.filter(deptnum__icontains=nospacesstring)))

        return sorted(list(c1), key=lambda x: x.deptnum, reverse=False)

    # either define a limit or an exact credit value to check. Limits are inclusive.
    @staticmethod
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
    @staticmethod
    def removeCourseWithSections(department, number):

        primarykey = department + str(number)
        try:

            Course.objects.get(pk=primarykey).delete()
            return True

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Course")
            return False

    @staticmethod
    def modifyCreditsForCourse(department, number, credits):

        try:
            C = Course.objects.get(pk=department + str(number))
            C.credits = credits
            C.save()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot modify Credits")
            return False

    @staticmethod
    def addCourse(name, number, department, credits=None):

        if len(Course.objects.filter(pk=department + str(number))) is not 0:
            logger.warn("Course already exists: " + department + str(number) + ". Cannot add")
            return False  # Course already exisits

        else:
            c = Course(name=name, department=department, number=number, deptnum=department + str(number))
            if credits is not None:
                c.credits = credits

            c.save()
            return True

    @staticmethod
    def addLectureToCourse(section, department, number, starttime, endtime, days, semester, location, isOnline):

        try:
            c = Course.objects.get(pk=(department + str(number)))
            e = Event(days=days, starttime=starttime, endtime=endtime, location=location,
                      semester=semester)
            e.save()
            l = Lecture(section=section, semester=semester, isOnline=isOnline, event=e)
            l.save()
            c.lecture_set.add(l)
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot add to Course")
            e.delete()
            l.delete()
            return False
        except django.db.IntegrityError:
            e.delete()
            l.delete()
            logger.warn("Lecture already in DB: {}{}, {}-{}. Cannot add to Course".format(department, number, section,
                                                                                            semester))
            return False

    @staticmethod
    def removeLectureFromCourse(section, department, number, semester):  #removes any labs/tut under

        primarykey = department + str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.lecture_set.get(semester=semester, section=section).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lecture.DoesNotExist:
            logger.warn(
                "Lecture not found: {}{}, {}-{}. Cannot remove from Course".format(department, number, section,
                                                                                     semester))
            return False

    @staticmethod
    def addLabToCourse(section, department, number, starttime, endtime, days, semester, location, lecturesection, tutorialsection = None):

        try:
            e = Event(days=days, starttime=starttime, endtime=endtime, location=location, semester=semester)
            e.save()
            lab = Lab(section=section, event=e)


            lab.save()
            #Below, we try to add a lab to a course if the lab exists, otherwise we throw an exception

            c = Course.objects.get(pk=(department + str(number)))
            c.lab_set.add(lab)
            lecture = c.lecture_set.get(semester=semester, course=c, section=lecturesection)
            lecture.lab_set.add(lab)

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot add lab to Course")
            e.delete()
            lab.delete()
            return False
        except Lecture.DoesNotExist:
            e.delete()
            lab.delete()
            logger.warn("Lecture not found: " + department + str(number) + ". Cannot add lab to Course")
            return False



        #Once the lab has been added to the course, we search for the tutorial linked with the section
        # and add try to add the lab to the tutorial
        if tutorialsection is not None:
            tutorial = Tutorial.objects.get(section=tutorialsection, course=c)
            tutorial.lab_set.add(lab)

    @staticmethod
    def removeLabFromCourse(section, department, number, semester):

        #Try to get the course with the primary key, if it is available, delete the lab that is inside of it
        primarykey = department + str(number)
        try:
            C = Course.objects.get(pk=primarykey)
            C.lab_set.get(event__semester=semester, section=section).delete()
            return True
        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lab.DoesNotExist:
            logger.warn("Lab not found, it cannot remove from Course")
            return False

    @staticmethod
    def addTutorialToCourse(section, department, number, semester, starttime, endtime, days, location, lecturesection):

        try:
            c = Course.objects.get(pk=(department + str(number)))
            e = Event(days=days, starttime=starttime, endtime=endtime, location=location,
                      semester=semester)
            e.save()
            tut = Tutorial(section=section, event=e)
            tut.save()
            c.tutorial_set.add(tut)
            lecture = c.lecture_set.get(semester=semester, section=lecturesection, course=c)
            lecture.tutorial_set.add(tut)
            return True

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot add to Course")
            tut.delete()
            e.delete()
            return False
        except django.db.IntegrityError:
            logger.warn("Tutorial already in DB, it cannot be added to courses".format(department, number, section, semester))
            tut.delete()
            e.delete()
            return False

    @staticmethod
    def removeTutorialFromCourse(section, department, number, semester):

        primarykey = department + str(number);
        try:
            C = Course.objects.get(pk=primarykey)
            C.tutorial_set.get(event__semester=semester, section=section).delete()
            return True

        except Course.DoesNotExist:
            logger.warn("Course not found: " + department + str(number) + ". Cannot remove Lecture from Course")
            return False
        except Lecture.DoesNotExist:
            logger.warn(
                "Lecture not found: {}{}, {}-{}. Cannot remove from Course".format(department, number, section,
                                                                                     semester))
            return False
        except Tutorial.DoesNotExist:
            logger.warn("Tutorial not found. It cannot be removed from the course.")
            return False

    # When given a section returns if this is Tutorial, Lab or Lecture. Functionality is used repeatedly elsewhere.
    @staticmethod
    def typeOfSection(section):

        typeofsection = str(type(section))

        if "Lecture" in typeofsection:
            return "Lecture"
        else:
            if "Lab" in typeofsection:
                return "Lab"
            else:
                return "Tutorial"

    @staticmethod
    # When given a section returns if it has tutorials. Functionality is used repeatedly elsewhere.
    def hasTutorial(section):

        if CourseCatalog.typeOfSection(section) == "Lecture":
            if len(section.tutorial_set.all()) == 0:
                return False
            else:
                return True
        if CourseCatalog.typeOfSection(section) == "Tutorial":
            return True

        if CourseCatalog.typeOfSection(section) == "Lab":
            if section.tutorial is not None:
                return True
            else:
                return False

    @staticmethod
    # When given a section returns if it has labs. Functionality is used repeatedly elsewhere.
    def hasLab(section):

        if CourseCatalog.typeOfSection(section) == "Lecture" or CourseCatalog.typeOfSection(section) == "Tutorial":
            if len(section.lab_set.all()) == 0:
                return False
            else:
                return True

        if CourseCatalog.typeOfSection(section) == "Lab":
            return True

    @staticmethod
    def coursesWithMetPrereqs(student, semester, year):
        # TODO: Have a extra parameters that come from the generation page, indicating classes they are taking. via POST?

        metprereq = []
        courselist = Course.objects.all().filter(lecture__semester=semester) # start with a list of all courses offered in that semester
        courseswithnoprereq = Course.objects.all().filter(prerequisites__isnull=True)
        #list of prereq and courses, individually packaged
        prereqdict = Course.objects.values("deptnum","prerequisites").exclude(prerequisites__isnull=True)

        coursesTaken = student.academicRecord.coursesTaken.all()  # start creating list of all taken courses
        if student.academicRecord.mainSchedule is not None:
            for schedules in student.academicRecord.mainSchedule.objects.all():
                if semester == "Summer1": # Only take into account courses being taken in summer of same year
                    if schedules.year <= year and schedules.semester == "Summer1":
                        for lecture in schedules.lecturelist.objects.all():
                            coursesTaken.append(lecture.course)
                elif semester == "Summer2": # Only take into account courses being taken in summer of same year
                    if schedules.year <= year and schedules.semester == "Summer2":
                        for lecture in schedules.lecturelist.objects.all():
                            coursesTaken.append(lecture.course)
                elif semester == "Fall": # Only take into account courses being taken in summer amd Fall of same year
                    if schedules.year <= year and (schedules.semester == "Summer" or schedules.semester == "Fall"):
                        for lecture in schedules.lecturelist.objects.all():
                            coursesTaken.append(lecture.course)
                elif semester == "Winter": # take into account everthing in same year
                    if schedules.year <= year:
                        for lecture in schedules.lecturelist.objects.all():
                            coursesTaken.append(lecture.course)

        # full list of courses taken that can be used as prerequisites

        for course in coursesTaken:
            for prereq in prereqdict:
                if course.deptnum == prereq["prerequisites"]:
                    metprereq.append(prereq)

        unmetprereq = [prereq for prereq in prereqdict if prereq not in metprereq]

        for prereq in unmetprereq:
            courselist = courselist.exclude(pk=prereq["deptnum"])

        return sorted(list(set(list(courselist))), key=lambda x: x.deptnum, reverse=False)  # remove duplicates and sort

    @staticmethod
    def seralizeCourseForSemester(specificcourse, semester=None):

        prereqs = []
        for i in specificcourse.prerequisites.all():
            prereqs.append(i.deptnum)

        allLectures = specificcourse.lecture_set.all()

        if semester is not None:
            allLectures = allLectures.filter(semester=semester)

        lectures = []
        # build a dictionary with all info related to the course
        for lect in allLectures:
            tutorials = []
            allTutorials = lect.tutorial_set.all()

            for tut in allTutorials:
                allLabs = tut.lab_set.all()
                labs = []

                for lab in allLabs:
                    labs.append({"section": lab.section,
                                 "days": lab.event.days,
                                 "starttime": lab.event.getActualStart(),
                                 "endtime": lab.event.getActualEnd(),
                                 "location": lab.event.location})

                tutorials.append({"section": tut.section,
                                  "days": tut.event.days,
                                  "starttime": tut.event.getActualStart(),
                                  "endtime": tut.event.getActualEnd(),
                                  "location": tut.event.location,
                                  "lab": labs})

            if len(allTutorials) == 0 and len(lect.lab_set.all()) != 0:
                allLabs = lect.lab_set.all()
                labs = []

                for lab in allLabs:
                    labs.append({"section": lab.section,
                                 "days": lab.event.days,
                                 "starttime": lab.event.getActualStart(),
                                 "endtime": lab.event.getActualEnd(),
                                 "location": lab.event.location})

                tutorials.append({"section": None,
                                  "lab": labs})

            lectures.append({"semester": lect.semester,
                             "section": lect.section,
                             "days": lect.event.days,
                             "starttime": lect.event.getActualStart(),
                             "endtime": lect.event.getActualEnd(),
                             "prof": lect.prof,
                             "location": lect.event.location,
                             "tutorial": tutorials})


        course_info = {"department": specificcourse.department,
                       "number": specificcourse.number,
                       "name": specificcourse.name,
                       "credits": specificcourse.credits,
                       "prereq": prereqs,
                       "lectures": lectures}
        serialized = json.dumps(course_info)

        return course_info  # or does it return serialized ?



