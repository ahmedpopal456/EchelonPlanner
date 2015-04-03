import re
import os
# from app.subsystem.courses import Course
from app.subsystem.courses.academicprogram import AcademicProgram
from app.subsystem.courses.course import Course
from app.subsystem.courses.option import Option
# from app.subsystem.courses import AcademicProgram
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Populates credits from json file to correct errors'

    def handle(self, *args, **options):
        # print(os.getcwd())

        gameslist = open(os.getcwd()+"\\app\\management\\commands\\computergamescourse.txt", "r").readlines()
        avionicslist = open(os.getcwd()+"\\app\\management\\commands\\avionicscourses.txt", "r").readlines()
        webcourselist = open(os.getcwd()+"\\app\\management\\commands\\webcourses.txt", "r").readlines()
        generalcourseslist = open(os.getcwd()+"\\app\\management\\commands\\generalcourses.txt", "r").readlines()
        P = AcademicProgram(name="SOEN", credits=120)

        for lines in gameslist:
            dptnum = re.search('[A-Z]{4}\d{3}', lines)
            dptnum = dptnum.group(0)
            dpt = dptnum[:4]
            num = dptnum[-3:]

            TechnicalType = re.search("Technical", lines)
            TechnicalStarType = re.search("Tech\W", lines)
            ScienceType = re.search("Science", lines)
            GeneralEleType = re.search("GeneralElective", lines)
            RequiredType = re.search("Required", lines)
            RequiredStarType = re.search("Requir\W", lines)



            if not RequiredType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=6, atleast_one=False)
                O.save()

            elif not RequiredStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredStarType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=6, atleast_one=True)
                O.save()

            elif not GeneralEleType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, GeneralEleType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=5, atleast_one=False)
                O.save()

            elif not ScienceType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, ScienceType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=7, atleast_one=False)
                O.save()

            elif not TechnicalType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=8, atleast_one=False)
                O.save()

            elif not TechnicalStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalStarType, P.name, "1st option")
                O = Option(course=C, academicprogram=P, option=1, type=8, atleast_one=True)
                O.save()


        for lines in avionicslist:
            dptnum = re.search('[A-Z]{4}\d{3}', lines)
            dptnum = dptnum.group(0)
            dpt = dptnum[:4]
            num = dptnum[-3:]

            TechnicalType = re.search("Technical", lines)
            TechnicalStarType = re.search("Tech\W", lines)
            ScienceType = re.search("Science", lines)
            GeneralEleType = re.search("GeneralElective", lines)
            RequiredType = re.search("Required", lines)
            RequiredStarType = re.search("Requir\W", lines)



            if not RequiredType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=6, atleast_one=False)
                O.save()

            elif not RequiredStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredStarType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=6, atleast_one=True)
                O.save()

            elif not GeneralEleType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, GeneralEleType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=5, atleast_one=False)
                O.save()

            elif not ScienceType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, ScienceType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=7, atleast_one=False)
                O.save()

            elif not TechnicalType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=8, atleast_one=False)
                O.save()

            elif not TechnicalStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalStarType, P.name, "3rd option")
                O = Option(course=C, academicprogram=P, option=3, type=8, atleast_one=True)
                O.save()


        for lines in webcourselist:
            dptnum = re.search('[A-Z]{4}\d{3}', lines)
            dptnum = dptnum.group(0)
            dpt = dptnum[:4]
            num = dptnum[-3:]

            TechnicalType = re.search("Technical", lines)
            TechnicalStarType = re.search("Tech\W", lines)
            ScienceType = re.search("Science", lines)
            GeneralEleType = re.search("GeneralElective", lines)
            RequiredType = re.search("Required", lines)
            RequiredStarType = re.search("Requir\W", lines)



            if not RequiredType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=6, atleast_one=False)
                O.save()

            elif not RequiredStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredStarType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=6, atleast_one=True)
                O.save()

            elif not GeneralEleType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, GeneralEleType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=5, atleast_one=False)
                O.save()

            elif not ScienceType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, ScienceType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=7, atleast_one=False)
                O.save()

            elif not TechnicalType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=8, atleast_one=False)
                O.save()

            elif not TechnicalStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalStarType, P.name, "2nd option")
                O = Option(course=C, academicprogram=P, option=2, type=8, atleast_one=True)
                O.save()


        for lines in generalcourseslist:
            dptnum = re.search('[A-Z]{4}\d{3}', lines)
            dptnum = dptnum.group(0)
            dpt = dptnum[:4]
            num = dptnum[-3:]

            TechnicalType = re.search("Technical", lines)
            TechnicalStarType = re.search("Tech\W", lines)
            ScienceType = re.search("Science", lines)
            GeneralEleType = re.search("GeneralElective", lines)
            RequiredType = re.search("Required", lines)
            RequiredStarType = re.search("Requir\W", lines)



            if not RequiredType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=6, atleast_one=False)
                O.save()

            elif not RequiredStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, RequiredStarType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=6, atleast_one=True)
                O.save()

            elif not GeneralEleType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, GeneralEleType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=5, atleast_one=False)
                O.save()

            elif not ScienceType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, ScienceType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=7, atleast_one=False)
                O.save()

            elif not TechnicalType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=8, atleast_one=False)
                O.save()

            elif not TechnicalStarType is None:
                C = Course.objects.get(pk=dptnum)
                # print(C.deptnum, TechnicalStarType, P.name, "4th option")
                O = Option(course=C, academicprogram=P, option=4, type=8, atleast_one=True)
                O.save()
