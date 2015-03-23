from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!

    homephone = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    cellphone = models.IntegerField(null=False, blank=False, default=0, primary_key=False)
    address = models.CharField(max_length=120, null=False, blank=False, default="", primary_key=False)

def __unicode__(self):
    return self.user.username


def __init__(self):
    self.__IDNumber = None
