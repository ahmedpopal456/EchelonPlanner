import re
import os
os.chdir("/")
# from app.subsystem.courses import Course
from app.subsystem.database.coursecatalog import *
# from app.subsystem.courses import AcademicProgram
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Populates credits from json file to correct errors'

    def handle(self, *args, **options):
        gameslist = open("computergamescourse.txt", "r").readlines()
        P = AcademicProgram(name="SOEN", credits=120, )
        for lines in gameslist:
            dptnum = re.search('[A-Z]{4} \d{3}', lines)
            T = re.search('[A-Z]{-10:}', lines)
            try:
                dptnum = dptnum.group(0)
                dpt = dptnum[:4]
                num = dptnum[-3:]
                T = T.group(0)
                if T == "  Required" :
                    C = Course.objects.get(pk=dptnum)
                    print(C.name, P.name, "games", "required")
                    #Option1= Option(course=C, academicprogram=P, option=1, type=6, atleast_one=False)
            except:

                T = ""
