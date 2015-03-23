from django.db import models


class Course(models.Model):

    def __str__(self):
        return self.deptnum

    def addStudent(IDNumber):
        pass

    def removeStudent(IDNumber):
        pass


    name = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    department = models.CharField(max_length=120, null=False, blank=False, default="SOEN", primary_key=False)
    number = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    deptnum = models.CharField (max_length=120, primary_key=True, default="SOEN101") # concat of dept and num
    type = models.CharField(max_length=120, null=True, blank=True, primary_key=False) # scrapper doesn't know type yet
    credits = models.FloatField(default=0, primary_key=False)
    prerequisites = models.ManyToManyField("self", null=True, blank=True)
    #equivalence = models.ForeignKey(null = True, blank= True) #scrapper doesn't know equivalence
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp

    class Meta:
        app_label = 'app'
        managed= True