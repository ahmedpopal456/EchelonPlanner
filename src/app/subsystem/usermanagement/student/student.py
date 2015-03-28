from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    # This line is required. Links to a User model instance.
    user = models.OneToOneField(User)

    # Additional Stuff
    homephone = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    cellphone = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    address = models.CharField(max_length=120, null=False, blank=False, default="", primary_key=False)
    IDNumber = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    #somer = models.CharField(max_length=120, null=True, blank=True, default="")

    def __unicode__(self):
        return self.user.username

    class Meta:
        app_label = 'app'
        managed= True