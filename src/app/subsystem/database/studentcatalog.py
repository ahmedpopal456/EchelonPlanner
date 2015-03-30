from app.subsystem.usermanagement.student import Student
from django.contrib.auth.models import User
import django.db
import logging

logger = logging.getLogger(__name__)

class StudentCatalog(object):

        @staticmethod

        def getStudent(username):

            try:
                user1 = set(list(User.objects.filter(name=username)))
                studentuser = set(list(Student.objects.filter(user_id=user1.id)))

                if (user1.len() is not 0) and (studentuser.len() is not 0):
                    return studentuser[0]

            except Student.DoesNotExist:
                logger.warn("Following Student does not exist")
                return False













	# def enrollStudent(student):
	# 	pass
    #
	# def removeStudent(student):
	# 	pass
    #
	# def __init__(self):
	# 	pass


