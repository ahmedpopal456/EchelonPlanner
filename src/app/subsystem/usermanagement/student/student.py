from django.contrib.auth.models import User
from django.db import models
from .studentrecord import StudentRecord


class Student(models.Model):
    # This line is required. Links to a User model instance.
    user = models.OneToOneField(User)
    # Student's unique academic record
    academicRecord = models.OneToOneField(StudentRecord, null=True)

    # Additional Stuff, mostly fluff
    homephone = models.CharField(max_length=15, null=False, blank=False, default="+1-XXX-XXX-XXXX", primary_key=False)
    cellphone = models.CharField(max_length=15, null=False, blank=False, default="XXX-XXX-XXXX", primary_key=False)
    address = models.CharField(max_length=120, null=False, blank=False, default="", primary_key=False)
    IDNumber = models.IntegerField(null=False, blank=False, default=0, primary_key=False)

    def __unicode__(self):
        specificInfo = {}
        specificInfo['IDNumber']=str(self.IDNumber)
        specificInfo['address']=str(self.address)
        specificInfo['homephone']=str(self.homephone)
        specificInfo['cellphone']=str(self.cellphone)
        return specificInfo

    class Meta:
        app_label = 'app'
        managed = True

# End class Student