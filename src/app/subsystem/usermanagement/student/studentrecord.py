from django.contrib.auth.models import User
from django.db import models
from app.subsystem.courses.course import Course
from app.subsystem.courses.academicprogram import AcademicProgram

#######################################################################################################################
# NOTE: For class StudentRecord, registeredCourses and coursesTaken CONFLICT for being defined similarly
#       A Lazy solution for this conflict is the use of the 'related_name' attribute. This, however, means that it
#       is problematic to inherit from this class in the future without causing a problematic database schema.
#######################################################################################################################


class StudentRecord(models.Model):
    # Student Related Information
    academicProgram = models.ForeignKey(AcademicProgram)
    registeredCourses = models.ManyToManyField(Course, null=True, blank=True, symmetrical=False,related_name="current_semester_course")
    coursesTaken = models.ManyToManyField(Course, null=True, blank=True, symmetrical=False, related_name="course_previously_taken")
    # scheduleCache = models.ManyToManyField(Schedule, null=True, blank=True, symmetrical=False)
    # Information related to academic performance and progress
    GPA = models.FloatField(default=4.0, primary_key=False)
    currentStanding = models.CharField(max_length=120, null=False, blank=False, default="Good", primary_key=False)
    currentCredits = models.FloatField(default=0, primary_key=False)
    remainingCredits = models.FloatField(default=0, primary_key=False)

    def viewStudentRecord(self):
        pass

    def deregisterCourse(self, course):
        pass

    def registerCourse(self, course):
        pass

    def listProgramCourses(self):
        pass

    def __init__(self):
        self.coursesTaken = None

    class Meta:
        app_label = 'app'
        managed= True

# End class StudentRecord