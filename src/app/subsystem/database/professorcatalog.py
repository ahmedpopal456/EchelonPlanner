import logging
import django.db
from django.contrib.auth.models import User
from app.subsystem.usermanagement.professor.professor import Professor
logger = logging.getLogger(__name__)

class ProfessorCatalog(object):

    def getProfessor(username):

        try:
            user1 = set(list(User.objects.filter(name=username)))
            professor1 = set(list(Professor.objects.filter(user_id=user1.id)))

            if (user1.len() is not 0) and (professor1.len() is not 0):

                return professor1[0]

        except Professor.DoesNotExist:
            logger.warn("Professor does not exist")
            return False