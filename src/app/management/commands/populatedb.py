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
            name = course["name"]
            department = course["department"]
            number = course["number"]
            deptnum = (course["department"]+str(course["number"])).replace(" ","")
            credits = course["Credits"]
            isOnline = False
            t = None
            try:
                c = Course(name=name, department=department, number=number, deptnum=deptnum,credits=credits, yearSpan="14-15")

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
                    l = Lecture(section=section, session = semester, isOnline=isOnline, event=e)
                    c.lecture_set.add(l)
                    c.save()
                    for tutorial in lecture["tutorial"]:
                        if 'starttime' in tutorial:
                            endtime = tutorial["endtime"]
                            starttime = tutorial["starttime"]
                            location = tutorial["location"]
                            days = tutorial["days"]
                            e = Event(days =days, starttime = starttime, endtime=endtime, building = location, location = location,
                              semester = semester)
                            t = Tutorial(section=section, event=e, course=c, lecture=l)
                            l.tutorial_set.add(t)
                        for lab in tutorial["lab"]:
                            endtime = lab["endtime"]
                            starttime = lab["starttime"]
                            location = lab["location"]
                            days = lab["days"]
                            e = Event(days =days, starttime = starttime, endtime=endtime, building = location, location = location,
                              semester = semester)
                            lab = Lab(section=section, event = e, course=c, lecture=l)
                            if t is not None:
                                t.lab_set.add(lab)
            except:
                logger.warn("Course or lecture or lab or tutorial already exists: "+deptnum)