from django.contrib.auth.models import User
from django.db import models


class Professor(models.Model):
    user = models.OneToOneField(User)
    isEngineer = models.BooleanField(default=False, primary_key=False)

    def __unicode__(self):
        return self.user.username

    class Meta:
        app_label = 'app'
        managed= True

# End class Professor

