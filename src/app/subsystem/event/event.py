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

    # Location/Place Variables For Frontend, easy access: event.location
    building = models.CharField (max_length=120, default="SGW H", null=True, blank=True)
    room = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    location = models.CharField (max_length=120, default="SGW H101") # This is the only field of actual use

    # Validity Variables
    semester = models.CharField(max_length=120, )
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp

    #Recurance (have not implemented yet)

    def __str__(self):
        return (self.semester+" "+self.days+" "+str(self.starttime)+"-"+str(self.endtime)+ " "+self.location)

    # List of bool function for front end to check day #
    def isMonday(self):

        if "M" in self.days:
            return True
        else:
            return False

    def isTuesday(self):

        if "T" in self.days:
            return True
        else:
            return False

    def isWednesday(self):

        if "W" in self.days:
            return True
        else:
            return False

    def isThursday(self):

        if "J" in self.days:
            return True
        else:
            return False

    def isFriday(self):

        if "F" in self.days:
            return True
        else:
            return False

    def isSaturday(self):

        if "S" in self.days:
            return True
        else:
            return False

    def isSunday(self):

        if "D" in self.days:
            return True
        else:
            return False

    def isOnline(self):

        if "-------" in self.days:
            return True
        else:
            return False

    #END of day checking functions#

    # Next two functions allow frontend to get the start/end time rounded to the nearest 15minutes
    def getRoundedStart(self):

        differencefromfifteen = (self.starttime.minute)%15
        if differencefromfifteen == 0:
            return self.starttime.strftime("%H:%M")
        else:
            timetoadd = datetime.timedelta(minutes=(15 - differencefromfifteen))
            returntime = datetime.datetime.combine(datetime.datetime.today(), self.starttime)+timetoadd

            return returntime.strftime("%H:%M")

    def getRoundedEnd(self):

        differencefromfifteen = self.endtime.minute % 15
        if differencefromfifteen == 0:
            return self.endtime.strftime("%H:%M")
        else:
            timetoadd = datetime.timedelta(minutes=(15 - differencefromfifteen))
            returntime = datetime.datetime.combine(datetime.datetime.today(), self.endtime)+timetoadd

            return returntime.strftime("%H:%M")

    #end of rounding functions

    # Allows frontend to get actual start/end to display as a string
    def getActualStart(self):

        return self.starttime.strftime("%H:%M")

    def getActualEnd(self):

        return self.endtime.strftime("%H:%M")

    # returns duration as an int of number of 15minute blocks.
    # Rounded. Might need testing with boundary conditions. i.e 00:05 to 00:55 should return 3 blocks (same as 00:15-00:00)

    def getDuration(self):

        endtimeobject = datetime.datetime.combine(datetime.datetime.today(), self.endtime)
        starttimeobject = datetime.datetime.combine(datetime.datetime.today(), self.starttime)
        duration = endtimeobject - starttimeobject

        seconds = duration.total_seconds()

        numberofblocks = round(seconds/900, 0)

        return numberofblocks

    class Meta:
        app_label = 'app'
        managed = True

# End Class Event


