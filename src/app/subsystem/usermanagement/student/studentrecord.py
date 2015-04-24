from django.contrib.auth.models import User
from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.courses.academicprogram import AcademicProgram
from app.subsystem.schedule import Schedule
import logging

logger = logging.getLogger(__name__)


#######################################################################################################################
# NOTE: For class StudentRecord, registeredCourses and coursesTaken CONFLICT for being defined similarly
#       A Lazy solution for this conflict is the use of the 'related_name' attribute. This, however, means that it
#       is problematic to inherit from this class in the future without causing a problematic database schema.
#######################################################################################################################


class StudentRecord(models.Model):
    # Student Related Information
    academicProgram = models.ForeignKey(AcademicProgram, null=True, blank=False)
    registeredCourses = models.ManyToManyField(Course, null=True, blank=True, symmetrical=False, related_name="current_semester_course")
    coursesTaken = models.ManyToManyField(Course, null=True, blank=True, symmetrical=False, related_name="course_previously_taken")
    scheduleCache = models.ManyToManyField(Schedule, null=True, blank=True, symmetrical=False, related_name="all_generated_schedules")
    mainSchedule = models.OneToOneField(Schedule, null=True, blank=True, related_name="main_schedule")

    # Information related to academic performance and progress
    GPA = models.FloatField(default=4.0, primary_key=False)
    currentStanding = models.CharField(max_length=120, null=False, blank=False, default="Good", primary_key=False)
    currentCredits = models.FloatField(default=0, primary_key=False)
    remainingCredits = models.FloatField(default=120, primary_key=False)

    def viewStudentRecord(self):
        pass

    def deregisterCourse(self, course):
        pass

    def registerCourse(self, course):
        pass

    def listProgramCourses(self):
        pass

    def moveScheduleFromCacheToMain(self):
        semester_list = ["Summer1", "Summer2", "Fall", "Winter"]
        # if self.mainSchedule:  # Delete the previously kept schedule if needed.
        #     self.mainSchedule.delete()

        # Go find a new one
        for i in range(1, 6):
            cached_schedules = self.scheduleCache.filter(year=i)
            if cached_schedules:
                for j in range(0, 4):
                    possible_replacement = cached_schedules.filter(semester=semester_list[j])
                    if possible_replacement:
                        print("Replaced Main Schedule")
                        self.mainSchedule = possible_replacement[0]  # Always take the first of the elements.
                        self.mainSchedule.save()
                        self.scheduleCache.remove(possible_replacement[0])
                        self.save()
                        return

        # IF we didn't find anything, assign an empty schedule
        if not self.scheduleCache.all():
            self.mainSchedule = None
            self.save()
        else:
            # Grab the first one!
            self.mainSchedule = self.scheduleCache.all()[0]

        return
    # end moveScheduleFromCacheToMain()

    # Used to move course from Main Schedule to CoursesTaken
    def passCourse(self, deptnum):

        self.mainSchedule.remove_course(deptnum)
        course_previously_taken = self.coursesTaken.filter(pk=deptnum)
        if not course_previously_taken:
            self.addTakenCourse(deptnum)

        # # Check if mainSchedule is empty, if so, then find replacement
        if len(self.mainSchedule.lectureList.all()) == 0:
            self.moveScheduleFromCacheToMain()

        return

    # Check if a schedule exists with the same year/semester,
    # returns the schedule if it is, if not, then None
    def doesScheduleForSemesterYearExist(self, year, semester):
        if self.mainSchedule:
            if self.mainSchedule.semester == semester and self.mainSchedule.year == year:
                return self.mainSchedule

            for schedule in self.scheduleCache.all():
                if schedule.year == year and schedule.semester == semester:
                    return schedule

        # If no schedule is found, then return None, safe to save
        return None






    # Used to move course from Main Schedule to CoursesTaken
    def failCourse(self, deptnum):

        self.mainSchedule.remove_course(deptnum)


        # Check if mainSchedule is empty, if so, then find replacement
        if len(self.mainSchedule.lectureList.all()) == 0:
            self.moveScheduleFromCacheToMain()

        #TODO: Failing a course should invalidate all future schedules
        # A few assumptions: a main schedule is the current year, all past must be courses taken,



    # Used to invalidate a schedule either in main or cache
    def removeSchedule(self, year, semester):

        if self.mainSchedule.semester == semester and self.mainSchedule.year == year:
            self.mainSchedule = None
            self.save()
            return
        else:
            for schedule in self.scheduleCache.all():
                if schedule.semester == semester and schedule.year == year:
                    self.scheduleCache.remove(schedule)
                    self.save()
                    return

    def removeScheduleWithPk(self, pk):

        if self.mainSchedule.semester == semester and self.mainSchedule.year == year:
            self.mainSchedule = None
            self.save()
            return
        else:
            for schedule in self.scheduleCache.all():
                if schedule.semester == semester and schedule.year == year:
                    self.scheduleCache.remove(schedule)
                    self.save()
                    return




    def addTakenCourse(self, deptnum):  # takes deptnum as primary key to add

        try:
            course = Course.objects.get(pk=deptnum)

            if course in self.coursesTaken.all():
                return False
            self.coursesTaken.add(course)

            # Need to decrement remaining credits
            remainingCredits = self.remainingCredits
            remainingCredits -= course.credits
            self.remainingCredits = remainingCredits

            #increment taken credits
            currentCredits = self.currentCredits
            currentCredits += course.credits
            self.currentCredits = currentCredits

            # Save record
            self.save()

            return True
        except Course.DoesNotExist:
            logger.warn("Course does not exist: "+deptnum)
            return False

    def removeTakenCourse(self, deptnum):  # takes deptnum as primary key to add

        try:
            course = Course.objects.get(pk=deptnum)
            self.coursesTaken.remove(course)

            # Need to increment remaining credits
            remainingCredits = self.remainingCredits
            remainingCredits += course.credits
            self.remainingCredits = remainingCredits

            #decrement taken credits
            currentCredits = self.currentCredits
            currentCredits -= course.credits
            self.currentCredits = currentCredits

            # Save record
            self.save()

            return True
        except Course.DoesNotExist:
            logger.warn("Course does not exist: "+deptnum)
            return False

    class Meta:
        app_label = 'app'
        managed = True

# End class StudentRecord