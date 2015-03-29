from django.contrib.auth.models import User
from django.db import models


class ProgramDirector(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=120, null=False, blank=False, default="CSE", primary_key=False)

    def __unicode__(self):
        return self.user.username

    class Meta:
        app_label = 'app'
        managed= True

# End class ProgramDirector