from app.subsystem.usermanagement.student import Student
from django.contrib.auth.models import User
import django.db
import logging

logger = logging.getLogger(__name__)

class StudentCatalog(object):

        @staticmethod

        def getStudent(username):

            try:
                user1 = User.objects.get(username=username)
                studentuser = Student.objects.get(user_id=user1.id)

                if user1 and studentuser:

                    return studentuser

            except Student.DoesNotExist or User.DoesNotExist:
                logger.warn("Student with this username does not exist")
                return False













	# def enrollStudent(student):
	# 	pass
    #
	# def removeStudent(student):
	# 	pass
    #
	# def __init__(self):
	# 	pass


