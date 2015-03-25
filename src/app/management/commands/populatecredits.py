from app.subsystem.courses.course import Course
import json
import logging
import django.core.exceptions

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populates credits from json file to correct errors'

    def handle(self, *args, **options):

        with open("prereq.json") as data_file:
            data = json.load(data_file)

        for course in data["Course"]:
            deptnum = course["department"]+course["number"]
            credits = course["Credits"]
            try:
                C = Course.objects.get(pk=deptnum)
                C.credits = credits
                C.save()
            except Course.DoesNotExist:
                logger.warn("Course doesn't exist: "+deptnum)