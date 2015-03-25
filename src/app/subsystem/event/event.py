from django.db import models
import datetime


class Event(models.Model):


    days = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    starttime= models.TimeField(null=False, blank=False, primary_key=False, default=datetime.time(0,0,0))
    endtime = models.TimeField(null=False, blank=False,  primary_key=False, default=datetime.time(0,0,0))
    #Recurance (have not implemented yet)
    building = models.CharField (max_length=120, default="SGW H", null=True, blank=True)
    room = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    location = models.CharField (max_length=120, default="SGW H101") # concat of dept and num
    semester = models.CharField(max_length=120, )
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp


    def __str__(self):
        return (self.semester+" "+self.days+" "+str(self.starttime)+"-"+str(self.endtime)+ " "+self.location)

    class Meta:
        app_label = 'app'
        managed = True


