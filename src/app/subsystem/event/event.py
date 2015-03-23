from django.db import models
class Event(models.Model):


    days = models.CharField(max_length=120, null=False, blank=False, default="Test", primary_key=False)
    starttime= models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    endtime = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    #Recurance (have not implemented yet)
    building = models.CharField (max_length=120, primary_key=True, default="SGW H")
    room = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    location = models.CharField (max_length=120, primary_key=True, default="SGW H101") # concat of dept and num
    #Semester (have not implemeted yet)
    yearSpan = models.CharField(max_length=120, null=True, blank=True, primary_key=False) #scrapper has this info, but not sure how to incorp

    class Meta:
        app_label = 'app'
        managed= True


