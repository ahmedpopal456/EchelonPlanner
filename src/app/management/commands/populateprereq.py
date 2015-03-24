__author__ = 'Thinesh'

from app.subsystem.courses.course import Course
import json
import logging
import django.core.exceptions

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Runs scrapper to populate DataBase'

    def handle(self, *args, **options):

        with open("prereq.json") as data_file:
            data = json.load(data_file)

        for course in data["Course"]:
            if len(course["prereq"]) != 0:
                try:
                    C = Course.objects.get(pk=(course["department"]+course["number"]))
                except:
                    logger.warn("Course doesn't exist: "+course["department"]+course["number"])

                for P in course["prereq"]:
                    P = P[:4]+P[-3:]
                    try:
                        Prereq = Course.objects.get(pk=P)
                        C.prerequisites.add(Prereq)
                    except:
                        logger.warn("Prereq doesn't exist: "+P)


