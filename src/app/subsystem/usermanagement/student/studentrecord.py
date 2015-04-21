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
        if self.mainSchedule:  # Delete the previously kept schedule if needed.
            self.mainSchedule.delete()

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
    # end moveScheduleFromCacheToMain()
        #
        #
        # # TODO: Logic needs to be reworked.
        # #       There's no guarantee that mainSchedule has no more courses when this is called!
        # # Means there are no more courses in MainSchedule and something from scheduleCache needs to take it's place:
        # elif len(self.mainSchedule.lectureList.all()) == 0 and len(self.scheduleCache.all()) > 0:
        #     currentYear = self.mainSchedule.year
        #     currentSemester = self.mainSchedule.semester
        #
        #     nextyearavailable = []
        #     tempnexthighestyear = 99
        #     allcacheSchedule = self.scheduleCache.all()
        #     # Find lowest years in schedule cache
        #     for schedule in allcacheSchedule:
        #         if tempnexthighestyear > schedule.year:
        #             tempnexthighestyear = schedule.year
        #     lowestSemesterAvailableList = []
        #     for schedule in allcacheSchedule:
        #         if schedule.year == tempnexthighestyear:
        #             nextyearavailable.append(schedule)
        #             lowestSemesterAvailableList.append(schedule.semester)
        #
        #     lowestSemester = ""
        #     if "Summer1" in lowestSemesterAvailableList:
        #         lowestSemester = "Summer1"
        #     elif "Summer2" in lowestSemesterAvailableList:
        #         lowestSemester = "Summer2"
        #     elif "Fall" in lowestSemesterAvailableList:
        #         lowestSemester = "Fall"
        #     elif "Winter" in lowestSemesterAvailableList:
        #         lowestSemester = "Winter"
        #
        #     for schedule in nextyearavailable:
        #         if schedule.semester == lowestSemester:
        #             self.mainSchedule = schedule
        #             self.scheduleCache.remove(schedule)
        #             self.save()
        # return  #CAREFUL WITH THE INDENTS!

    # Used to move course from Main Schedule to CoursesTaken
    def passCourse(self, deptnum):

        self.mainSchedule.remove_course(deptnum)
        self.addTakenCourse(deptnum)

        # Check if mainSchedule is empty, if so, then find replacement
        if len(self.mainSchedule.lectureList.all()) == 0:
            self.moveScheduleFromCacheToMain()

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


    def addTakenCourse(self, deptnum):  # takes deptnum as primary key to add

        try:
            course = Course.objects.get(pk=deptnum)
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