from django.test import TestCase
from ..database.coursecatalog import CourseCatalog as coursecatalog
from .schedulegenerator import ScheduleGenerator as schedGen
from .schedule import Schedule
from ..courses.course import Course as course
import django.db


class TestSchedule(TestCase):
    def setUp(self):
        self.myCourseCatalog = coursecatalog
        self.myCourseCatalog.addCourse("Test 1", 428, "COMP", 3.5)
        self.myCourseCatalog.addLectureToCourse("T", "COMP", 428, "11:45:00", "13:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TA", "COMP", 428, "Fall", "17:45:00", "19:00:00", "M------", "SGW H-454", "T")
        self.myCourseCatalog.labToCourse("TM", "COMP", 428,  "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "T", "TA")
        self.myCourseCatalog.addCourse("Test 2", 341, "SOEN", 3)
        self.myCourseCatalog.addLectureToCourse("V", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("VI", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "V")
        self.myCourseCatalog.labToCourse("VM", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.labToCourse("VN", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "V", "VI")
        self.myCourseCatalog.tutorialToCourse("VJ", "SOEN", 341, "Fall", "10:15:00", "11:30:00", "--W----", "SGW H-401", "V")
        self.myCourseCatalog.labToCourse("VO", "SOEN", 341, "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "V", "VJ")
        self.myCourseCatalog.labToCourse("VP", "SOEN", 341, "8:45:00", "10:00:00", "---R---", "Fall", "SGW H-821", "V", "VJ")
        self.myCourseCatalog.addLectureToCourse("T", "SOEN", 341, "13:45:00", "15:00:00", "--W-F--", "Fall", "SGW H-401", False)
        self.myCourseCatalog.tutorialToCourse("TI", "SOEN", 341, "Fall", "11:00:00", "12:15:00", "-T-----", "SGW H-401", "T")
        self.myCourseCatalog.labToCourse("TM", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "T", "TI")
        self.myCourseCatalog.labToCourse("TN", "SOEN", 341, "17:45:00", "19:00:00", "---R---", "Fall", "SGW H-821", "T", "TI")
        self.myCourseCatalog.tutorialToCourse("TJ", "SOEN", 341, "Fall", "10:15:00", "11:30:00", "--W----", "SGW H-401", "T")
        self.myCourseCatalog.labToCourse("TO", "SOEN", 341, "8:45:00", "10:00:00", "M------", "Fall", "SGW H-821", "T", "TJ")
        self.myCourseCatalog.labToCourse("TP", "SOEN", 341, "8:45:00", "10:00:00", "---R---", "Fall", "SGW H-821", "T", "TJ")

    def tearDown(self):
        self.myCourseCatalog.removeCourse("COMP", 428)
        self.myCourseCatalog.removeCourse("SOEN", 341)

    def test_addCourse_removeItem_lecture(self):
        """
            Tests that a lecture is added to schedule and then removed
        """
        myLecture = self.myCourseCatalog.searchCourses("COMP428")[0].lecture_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_course(myLecture)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myLecture)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

    def test_addCourse_removeItem_tutorial(self):
        """
            Tests that a tutorial and its lecture are added to schedule
            and then removed
        """
        myLecture = self.myCourseCatalog.searchCourses("COMP428")[0].lecture_set.all()[0]
        myTutorial = self.myCourseCatalog.searchCourses("COMP428")[0].tutorial_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_course(myTutorial)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myTutorial, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myTutorial)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

    def test_addCourse_removeItem_lab(self):
        """
            Tests that a lab and its accompanying tutorial and
            lecture are added to schedule and then removed
        """
        myLecture = self.myCourseCatalog.searchCourses("COMP428")[0].lecture_set.all()[0]
        myTutorial = self.myCourseCatalog.searchCourses("COMP428")[0].tutorial_set.all()[0]
        myLab = self.myCourseCatalog.searchCourses("COMP428")[0].lab_set.all()[0]
        mySchedule = Schedule()
        mySchedule.add_course(myLab)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertIn(self, myLab, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myTutorial, coursesInMySchedule, "The course was not added to the schedule")
        TestCase.assertIn(self, myLecture, coursesInMySchedule, "The course was not added to the schedule")
        mySchedule.remove_item(myLab)
        coursesInMySchedule = mySchedule.view_schedule()
        TestCase.assertEqual(self, len(coursesInMySchedule), 0, "The course was not removed from the schedule")

if __name__ == '__main__':
    TestCase.main()