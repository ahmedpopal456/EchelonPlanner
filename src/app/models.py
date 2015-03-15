from django.db import models


class Course(models.Model):

    def addStudent(IDNumber):
        pass

    def removeStudent(IDNumber):
        pass


    name = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    department = models.CharField(max_length=120, null=False, blank=False, default="SOEN", primary_key=False)
    number = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    deptnum = models.CharField (max_length=120, primary_key=True, default="SOEN101") # concat of dept and num
    type = models.CharField(max_length=120, null=True, blank=True, primary_key=False) # scrapper doesn't know type yet
    credits = models.IntegerField(default=0, primary_key=False)
    #prerequisites = models.ForeignKey(Course) # not sure how to relate to self
    #equivalence = models.ForeignKey(null = True, blank= True) #scrapper doesn't know equivalence
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp


class Lecture(models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False)
    session = models.CharField(max_length=120, default="Fall", primary_key=False)
    isOnline = models.BooleanField(default=False, primary_key=False)

    class Meta:
        unique_together = ('section', 'course')


class Tutorial(models.Model):
    section = models.CharField(max_length=120, default="A", primary_key=False)
    course = models.ForeignKey(Course, primary_key=False)
    tutorial = models.ForeignKey(Lecture, primary_key=False)

    class Meta:
        unique_together = ('section', 'course', 'tutorial')