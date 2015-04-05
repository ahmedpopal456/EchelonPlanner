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
    mainSchedule = models.ForeignKey(Schedule, null=True, blank=True, related_name="main_schedule")
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

    def addTakenCourse(self, coursestring):  # takes deptnum as primary key to add

        try:
            course = Course.objects.get(pk=coursestring)
            self.coursesTaken.add(course)
            return True
        except Course.DoesNotExist:
            logger.warn("Course does not exist: "+coursestring)
            return False

    class Meta:
        app_label = 'app'
        managed= True

# End class StudentRecord