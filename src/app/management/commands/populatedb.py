from app.subsystem.database.coursecatalog import *
import json
import logging
import django.core.exceptions

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populates credits from json file to correct errors'

    def handle(self, *args, **options):

        with open("database.json") as data_file:
            data = json.load(data_file)

        for course in data["Course"]:
            if course["department"] == "AERO" and course["number"] == " 482":
                name = course["name"]
                department = course["department"]
                number = course["number"]
                deptnum = (course["department"]+str(course["number"])).replace(" ","")
                credits = course["Credits"]
                isOnline = False
                t = None
                #try:
                c = Course(name=name, department=department, number=number, deptnum=deptnum,credits=credits, yearSpan="14-15")
                c.save()
                print(name, department, number,credits)
                for lecture in course["Lecture"]:
                    endtime = lecture["endtime"]
                    starttime = lecture["starttime"]
                    prof = lecture["prof"]
                    semester = lecture["semester"]
                    location = lecture["location"]
                    days = lecture["days"]
                    if "Online" in location:
                        isOnline = True
                    section = lecture["section"]
                    e = Event(days =days, starttime = starttime, endtime=endtime, location = location,
                              semester = semester)
                    e.save()
                    l = Lecture(section=section, semester = semester, isOnline=isOnline, event=e, prof=prof)
                    l.save()
                    c.lecture_set.add(l)
                    c.save()
                    print(section, semester, e, prof)
                    for tutorial in lecture["tutorial"]:
                        if 'starttime' in tutorial:
                            endtime = tutorial["endtime"]
                            starttime = tutorial["starttime"]
                            location = tutorial["location"]
                            days = tutorial["days"]
                            section = tutorial["section"]
                            e = Event(days =days, starttime = starttime, endtime=endtime, building = location, location = location,
                              semester = semester)
                            e.save()
                            t = Tutorial(section=section, event=e, course=c, lecture=l)
                            t.save()
                            l.tutorial_set.add(t)
                        for lab in tutorial["lab"]:
                            endtime = lab["endtime"]
                            starttime = lab["starttime"]
                            location = lab["location"]
                            days = lab["days"]
                            section = lab["section"]
                            e = Event(days =days, starttime = starttime, endtime=endtime, building = location, location = location,
                              semester = semester)
                            e.save()
                            lab = Lab(section=section, event = e, course=c, lecture=l)
                            lab.save()
                            if t is not None:
                                t.lab_set.add(lab)
        print("Finished populating courses")
        data_file.close()
            #except django.db.DatabaseError:
             #   logger.warn("Course or lecture or lab or tutorial already exists: "+deptnum)