from django.db import models
from django_enumfield import enum
import datetime

class RecurrenceType(enum.Enum):
    Daily = 1
    Weekly = 2
    BiWeekly = 3
    Monthly = 4
# End TypeChoices

class Event(models.Model):
    # Time Variables
    days = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    starttime= models.TimeField(null=False, blank=False, primary_key=False, default=datetime.time(0,0,0))
    endtime = models.TimeField(null=False, blank=False,  primary_key=False, default=datetime.time(0,0,0))

    # Location/Place Variables
    building = models.CharField (max_length=120, default="SGW H", null=True, blank=True)
    room = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    location = models.CharField (max_length=120, default="SGW H101") # concat of dept and num

    # Validity Variables
    semester = models.CharField(max_length=120, )
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp

    #Recurance (have not implemented yet)

    def __str__(self):
        return (self.semester+" "+self.days+" "+str(self.starttime)+"-"+str(self.endtime)+ " "+self.location)

    class Meta:
        app_label = 'app'
        managed = True

# End Class Event


