from ...subsystem.courses.course import Course
import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Running the scraper to populate the courses for the 400 level courses'

    def handle(self, *args, **options):

        Course400AndAbove = Course.objects.filter(number__gte=400)

        listof200leveldeptnum = ["ENGR 201",
                                "ENGR 202",
                                "ENGR 213",
                                "ENGR 233",
                                "ELEC 275",
                                "ENCS 282",
                                "SOEN 228",
                                "SOEN 287",
                                "COMP 232",
                                "COMP 248",
                                "COMP 249"]

        for C in Course400AndAbove:
            for P in listof200leveldeptnum:
                P = P[:4]+P[-3:]
                prereq = Course.objects.get(pk=P)
                if prereq not in C.prerequisites.all():
                    C.prerequisites.add(prereq)
                    print(prereq)
        print("Finished populating pre-reqs for 400 level courses")

